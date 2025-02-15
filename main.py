import pandas as pd
import os
import functions 

games = pd.read_csv("./games2024.csv")
# let's only use games in the Regular Season 
games = games[games['Week'] < 19]

teamA = "San Francisco 49ers"
teamB = "New York Giants"

functions.common_games(games, teamA, teamB)

functions.common_games_decision(games, teamA, teamB)

all_teams = pd.unique(games['Winner'])
functions.season_leaders(all_teams, games) 