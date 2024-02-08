import requests
import random

URL = "https://opentdb.com/api.php?amount=10&type=boolean"

response = requests.get(url=URL)
response.raise_for_status()
data = response.json()
i = 0
score = 0
questions = []

questions = [result["question"] for result in data["results"]]
correct_answers = [result["correct_answer"] for result in data["results"]]

def start():
	print("Welcome to the Quiz Game!")
	answer = input("Do you want to play (y/n)")
	if answer == y:
		return True
	else:
		return False


while(1):
	if start():
		answer = input(f"Q {questions[i]} :")
		if answer == correct_answers[i]:
			score += 1
		i += 1
		if i > len(questions):
			print("Out of questions")
			print(scoreboard())
	else:
		break

import pandas as pd

#global /class variable for leaderboard?
leaderboard = pd.DataFrame(columns = ['Name', 'Score'])

def start_game():
    starting = input("Do you want to start a new game? Y/N")
    if starting == "N":
        return False
    else:
        playername = input("What is your name? ")
        return playername
    
def return_score(score):
    print(f"Your score is {score}")

# def create_leaderboard():
#     leaderboard = pd.DataFrame()

def update_leaderboard(leaderboard, name, score):
    new_row = pd.DataFrame({'Name': [name], 'Score': [score]})
    updated_board = leaderboard.append(new_row)
    return updated_board

def show_leaderboard():
    print(leaderboard)

show_leaderboard()
leaderboard = update_leaderboard(leaderboard, 'jane', 10)
show_leaderboard()