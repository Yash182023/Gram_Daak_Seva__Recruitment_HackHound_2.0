import pandas as pd
import numpy as np

# Load the existing CSV file
file_path = 'C:/Users/sharm/OneDrive/Desktop/student_data/student_marks_with_total.csv'
df = pd.read_csv(file_path)

# Create a list of years
years = [2020, 2018, 2016, 2014]

# Create an empty DataFrame to store the year difficulty data
year_difficulty_df = pd.DataFrame(columns=['Year', 'Board_Name', 'Difficulty'])

# Generate random difficulty values for each year and board combination
for year in years:
    year_difficulty_data = []
    for board in df['Board_Name'].unique():
        difficulty = np.random.randint(1, 100)
        year_difficulty_data.append([year, board, difficulty])
    year_difficulty_df = pd.concat([year_difficulty_df, pd.DataFrame(year_difficulty_data, columns=['Year', 'Board_Name', 'Difficulty'])])

# Merge the original DataFrame with the year difficulty DataFrame
merged_df = pd.merge(df, year_difficulty_df, on='Board_Name', how='left')

# Save the merged DataFrame to a new CSV file
new_file_path = 'student_marks_with_year_difficulty_3_Columns.csv'
merged_df.to_csv(new_file_path, index=False)
