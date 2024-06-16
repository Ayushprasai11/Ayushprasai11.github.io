import pandas as pd
import os

# Path to the folder containing the CSV files
folder_path = "nba_files"

# List of file names without extensions
file_names = ['games', 'games_details', 'players', 'ranking', 'teams']

# Dictionary to hold DataFrames
dfs = {}

# Loop through the list of file names and read each one into a DataFrame
for file_name in file_names:
    file_path = os.path.join(folder_path, f'{file_name}.csv')
    dfs[file_name] = pd.read_csv(file_path)

# Top 5 Team Scoring Records
# Merging games and teams data to get team names
games_df = dfs['games']
teams_df = dfs['teams']

# Home team scores
home_team_scores = games_df[['GAME_ID', 'HOME_TEAM_ID', 'PTS_home']].rename(columns={'HOME_TEAM_ID': 'TEAM_ID', 'PTS_home': 'PTS'})
home_team_scores['HOME/AWAY'] = 'HOME'

# Away team scores
away_team_scores = games_df[['GAME_ID', 'VISITOR_TEAM_ID', 'PTS_away']].rename(columns={'VISITOR_TEAM_ID': 'TEAM_ID', 'PTS_away': 'PTS'})
away_team_scores['HOME/AWAY'] = 'AWAY'

# Concatenate home and away scores
team_scores = pd.concat([home_team_scores, away_team_scores])

# Merge with teams data to get team names
team_scores = pd.merge(team_scores, teams_df[['TEAM_ID', 'NICKNAME']], on='TEAM_ID')

# Sort by points scored in descending order
sorted_team_scores = team_scores.sort_values(by='PTS', ascending=False)

# Get top 5 team scoring records
top_5_team_scores = sorted_team_scores.head(5)
top_5_team_scores_display = top_5_team_scores[['NICKNAME', 'PTS', 'HOME/AWAY']]

# Display the top 5 team scoring records
print(top_5_team_scores_display)
