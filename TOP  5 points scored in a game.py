import pandas as pd
import os

# Set the folder name containing the CSV files
folder_name = 'nba_files'

# Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Construct the full path to the folder
folder_path = os.path.join(current_dir, folder_name)
print(f"Checking folder path: {folder_path}")

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"Error: Folder not found - {folder_path}")
else:
    print(f"Success: Folder found - {folder_path}")

    # List files in the folder
    files_in_folder = os.listdir(folder_path)
    print(f"Files in folder: {files_in_folder}")

    # List of file names without extensions
    file_names = ['games', 'games_details', 'players', 'ranking', 'teams']

    # Dictionary to hold DataFrames
    dfs = {}

    # Loop through the list of file names and read each one into a DataFrame
    for file_name in file_names:
        file_path = os.path.join(folder_path, f'{file_name}.csv')
        print(f"Checking file path: {file_path}")

        if os.path.exists(file_path):
            dfs[file_name] = pd.read_csv(file_path)
            print(f"Successfully read {file_path}")
        else:
            print(f"Error: File not found - {file_path}")

# Checking if essential data frames are loaded
if 'games_details' in dfs and 'players' in dfs:
    games_details_df = dfs['games_details']
    players_df = dfs['players']
    
    # Display the columns of the DataFrames
    print(f"games_details_df columns: {games_details_df.columns}")
    print(f"players_df columns: {players_df.columns}")

    # Merge games_details_df with players_df on PLAYER_ID
    merged_df = pd.merge(games_details_df, players_df, on='PLAYER_ID')
    print(f"Columns in merged_df after merge: {merged_df.columns}")

    # Sort by points scored in descending order
    sorted_df = merged_df.sort_values(by='PTS', ascending=False)

    # Keep track of unique scores and top scorers
    unique_scores = []
    top_scorers = []

    # Loop through the sorted DataFrame to find the top 5 unique high scoring performances
    for index, row in sorted_df.iterrows():
        if len(top_scorers) < 5:
            if row['PTS'] not in unique_scores:
                top_scorers.append(row)
                unique_scores.append(row['PTS'])
        else:
            break

    # Convert top_scorers list to a DataFrame for display
    top_scorers_df = pd.DataFrame(top_scorers)
    print(f"Top 5 unique highest scoring performances:\n{top_scorers_df[['PLAYER_NAME_x', 'PTS']]}")

else:
    print("Error: Essential data frames (games_details and players) are not loaded.")
