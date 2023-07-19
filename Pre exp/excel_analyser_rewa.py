import pandas as pd
import numpy as np
import os
import glob

def analyze_excel_data(name):
    folder_path = "data"
    csv_files = glob.glob(folder_path + "/*.csv")
    matching_files = [file for file in csv_files if os.path.basename(file).split('_')[0] == name]

    if matching_files:
        most_recent_csv = max(matching_files, key=os.path.getctime)
        df = pd.read_csv(most_recent_csv)
    else:
        print("No matching CSV files found.")

    df = pd.read_csv(most_recent_csv)

    # Select the desired columns
    selected_columns = [
        'total_score', 'Countdown', 'correct', 'trials.thisRepN', 'response.corr',
        'response_2.corr', 'response_3.corr'
    ]

    df = df[selected_columns]

    # Save the selected data to a new CSV file
    df['combined_corr'] = df[['response.corr', 'response_2.corr', 'response_3.corr']].sum(axis=1)
    df.drop(['response.corr', 'response_2.corr', 'response_3.corr'], axis=1, inplace=True)
    df.dropna(subset=['total_score'], inplace=True)

    ratios = [60, 60, 60, 60, 60, 60, 57, 57, 57, 57, 57, 57, 54, 54, 54, 54, 54, 54]

    # Calculate the number of repetitions needed
    repetitions = int(np.ceil(len(df) / len(ratios)))

    # Repeat the ratios pattern to match the length of the DataFrame
    ratios = ratios * repetitions
    ratios = ratios[:len(df)]
    df['dot_ratio'] = ratios

    replacement_dict = {
        'Countdown_2.5s.mp4': 2.5,
        'Countdown_2s.mp4': 2,
        'Countdown_1.5s.mp4': 1.5
    }

    # Replace values in the 'Countdown' column
    df['Countdown'] = df['Countdown'].replace(replacement_dict)

    target_accuracy = 0.8

    # Create a new column for accuracy
    df['accuracy'] = df['combined_corr'].apply(lambda x: 1 if x == 1.0 else 0)

    # Group the data by combination of columns and calculate average accuracy
    grouped = df.groupby(['Countdown', 'dot_ratio']).agg(average_accuracy=('accuracy', 'mean')).reset_index()

    # Find the combination with the closest average accuracy to the target
    closest_combination = grouped.iloc[(grouped['average_accuracy'] - target_accuracy).abs().argsort()[0]]

    result = {
        'closest_combination': {
            'Countdown': closest_combination['Countdown'],
            'dot_ratio': closest_combination['dot_ratio'],
            'average_accuracy': closest_combination['average_accuracy']
        }
    }

    combinations = [
        {'Countdown': 2.5, 'dot_ratio': 60},
        {'Countdown': 2.5, 'dot_ratio': 57},
        {'Countdown': 2.5, 'dot_ratio': 54},
        {'Countdown': 2, 'dot_ratio': 60},
        {'Countdown': 2, 'dot_ratio': 57},
        {'Countdown': 2, 'dot_ratio': 54},
        {'Countdown': 1.5, 'dot_ratio': 60},
        {'Countdown': 1.5, 'dot_ratio': 57},
        {'Countdown': 1.5, 'dot_ratio': 54}
    ]

    accuracy_df = pd.DataFrame(columns=['Countdown', 'dot_ratio', 'Accuracy'])

    for combination in combinations:
        subset = df[(df['Countdown'] == combination['Countdown']) & (df['dot_ratio'] == combination['dot_ratio'])]
        accuracy = subset['accuracy'].mean() * 100
        combination['Accuracy'] = accuracy
        accuracy_df = accuracy_df.append(combination, ignore_index=True)

    result['accuracy_data'] = accuracy_df
    return result

# Call the analyze_excel_data function
# output = analyze_excel_data(name)

