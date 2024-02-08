import requests
import pandas as pd
import random


URL = "https://opentdb.com/api.php?amount=10&type=boolean"

response = requests.get(url=URL)
response.raise_for_status()
data = response.json()
i = 0
score = 0
player_name = ""
questions = []

#global /class variable for leaderboard?
leaderboard = pd.DataFrame(columns = ['Name', 'Score'])

questions = [result["question"] for result in data["results"]]
correct_answers = [result["correct_answer"] for result in data["results"]]

def start_game():
	starting = input("Do you want to start a new game?: Y/N ")
	if starting == "N":
		return False
	else:
		playername = input("What is your name? ")
		return playername

def update_leaderboard(leaderboard,name, score):
	new_row = pd.DataFrame({'Name': [name], 'Score': [score]})
	updated_leaderboard = pd.concat([leaderboard,new_row])
	return updated_leaderboard

def show_leaderboard():
	print(leaderboard.groupby('Name').sum())

def scoreboard():
	return f"Thanks for playing! Your score was {score}"

while(1):
	name = start_game()
	if name == False:
		break
	else:
		while (i < len(questions)):
			answer = input(f"Q {questions[i]} : (True/False)")
			if answer == correct_answers[i]:
				score += 1
			i += 1
		print("Out of questions")
		i=0
		print(scoreboard())
		leaderboard = update_leaderboard(leaderboard, name, score)
		score = 0
		show_leaderboard()


