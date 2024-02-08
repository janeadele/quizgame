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