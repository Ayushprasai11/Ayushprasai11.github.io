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
    dfs[file_name] = pd.read_csv(file_path, low_memory=False)

# Best Free Throw Shooters

# Extract relevant columns
games_details_df = dfs['games_details'][['PLAYER_ID', 'PLAYER_NAME', 'FTM', 'FTA']]

# Group by player to get total free throws made and attempted
free_throw_stats = games_details_df.groupby(['PLAYER_ID', 'PLAYER_NAME']).sum().reset_index()

# Calculate free throw percentage
free_throw_stats['FT_PCT'] = free_throw_stats['FTM'] / free_throw_stats['FTA']

# Filter out players with less than a minimum number of attempts to ensure a meaningful percentage
min_attempts = 50
filtered_free_throw_stats = free_throw_stats[free_throw_stats['FTA'] >= min_attempts]

# Find the top 5 players with the highest free throw percentage
top_5_free_throw_shooters = filtered_free_throw_stats.sort_values(by='FT_PCT', ascending=False).head(5)

# Display the top 5 free throw shooters
print(top_5_free_throw_shooters[['PLAYER_NAME', 'FTM', 'FTA', 'FT_PCT']])
