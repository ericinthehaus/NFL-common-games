import pandas as pd
import os
os.getcwd()

games = pd.read_csv("./games2024.csv")
# let's only use games in the Regular Season 
games = games[games['Week'] < 19]

# Pick teams
teamA = "Washington Commanders"
teamB = "Detroit Lions"

# =======================================================
# -------------- Function with DataFrame ----------------
# =======================================================

def common_games(teamA=teamA, teamB=teamB): 
    winsA = games[games['Winner'] == teamA]['Loser']
    lossesA = games[games['Loser'] == teamA]['Winner']     
    winsB = games[games['Winner'] == teamB]['Loser']
    lossesB = games[games['Loser'] == teamB]['Winner']

    teamA_games = list(winsA) + list(lossesA) 
    teamB_games = list(winsB) + list(lossesB) 
    both_games  = set(teamA_games).union(teamB_games)

    df = pd.DataFrame({
        'opponent' : pd.Series(list(set(teamA_games).union(teamB_games)))
    })

    for x in range(0, len(df)):
        df.loc[x, "num_A"] = teamA_games.count(df['opponent'].iloc[x])
        df.loc[x, "num_B"] = teamB_games.count(df['opponent'].iloc[x])
        # wins:
        df.loc[x, "wins_A"] = list(winsA).count(df['opponent'].iloc[x])
        df.loc[x, "wins_B"] = list(winsB).count(df['opponent'].iloc[x])
        #losses:
        df.loc[x, "losses_A"] = list(lossesA).count(df['opponent'].iloc[x])
        df.loc[x, "losses_B"] = list(lossesB).count(df['opponent'].iloc[x])

    df = df[(df["num_A"] > 0) & (df["num_B"]>0)]

    h2h = ""
    if teamB in set(winsA) and teamA in set(winsB): 
        h2h = "Both teams beat each other this year."
    elif teamB in set(winsA):
        h2h = f"{teamA} beat {teamB}\n Total times: {winsA.tolist().count(teamB)}"
    elif teamA in set(winsB):
        h2h = (f"{teamB} beat {teamA}\n Total times: {winsB.tolist().count(teamA)}")
    else: 
        h2h = ("they did NOT play this year.")

    x1 = str(f"{teamA} versus {teamB} \n")
    
    x2 = str(f"Both teams played against: \n {df} \n \n")

    x3_a = str(f"Out of {sum(df['num_A'])} games, wins for {teamA} = {sum(df['wins_A'])} \n")
    x3_b = str(f"Out of {sum(df['num_B'])} games, wins for {teamB} = {sum(df['wins_B'])} \n")

    dff4 = list(df[(df["wins_A"] > 0) & (df["wins_B"] > 0)]['opponent'])
    x4 = str(f"\n Both teams beat:\n {dff4} \n")

    dff5 = list(df[(df["losses_A"] > 0) & (df["losses_B"] > 0)]['opponent'])
    x5 = str(f"Both teams lost to:\n {dff5} \n")

    x6 = "\n \t HEAD TO HEAD \n"
    
    f = open("results.txt", "w")
    f.write(x1)
    f.write(x2)
    f.write(x3_a)
    f.write(x3_b)
    f.write(x4)
    f.write(x5)
    f.write(x6)
    f.write(h2h)

    f.close()

###  Have fun here: 
common_games(teamA, teamB)
