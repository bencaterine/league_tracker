from classes import Team, Game
from schedule_games import schedule_games
from enter_results import enter_results
from view import view_schedule, view_results, view_standings


# INITIALIZATION

print("\nEnter your league's teams below. \
Be sure to use the format 'Team X, Team Y, Team Z':")

team_input = [x for x in input().split(", ")]

# list of teams in id order
teams = []
# dict of teams -> ids
teams_dict = {}
for i, team in enumerate(team_input):
    # var 'team' for each team
    teams.append(Team(str(team), i))
    teams_dict[str(team)] = i

# adjacency matrix for game schedule graph: games[hid][aid]
games = [[None for x in teams] for x in teams]
for i, row in enumerate(games):
    for j, game in enumerate(games[i]):
        if i != j:
            # game stored at graph location
            games[i][j] = Game(i, j)


# CONTROL FLOW

while(1):
    todo = input("\nWhat would you like to do next?\n\
   Schedule games:  1\n   Enter results:   2\n   View schedule:   3\n\
   View results:    4\n   View standings:  5\n   Done:            6\n\
Type the indicated number: ")
    print()
    if todo == '1':
        schedule_games(teams, teams_dict, games)
    elif todo == '2':
        enter_results(teams, teams_dict, games)
    elif todo == '3':
        view_schedule(teams, games)
    elif todo == '4':
        view_results(teams, games)
    elif todo == '5':
        view_standings(teams, games)
    elif todo == '6':
        exit = input("Are you sure you're done? Type 'exit' to finish: ")
        print()
        if exit == 'exit':
            break
