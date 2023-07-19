import pandas as pd
import numpy as np
import os
import glob

name="Annie"
folder_path = "data"
skip_csv_files = glob.glob(folder_path + "/*_2*.csv")
no_skip_csv_files = glob.glob(folder_path + "/*_1*.csv")

skip_matching_files = [file for file in skip_csv_files if os.path.basename(file).split('_')[0] == name]
no_skip_matching_files = [file for file in no_skip_csv_files if os.path.basename(file).split('_')[0] == name]

if skip_matching_files:
    most_recent_skip_csv = max(skip_matching_files, key=os.path.getctime)
    df_skip = pd.read_csv(most_recent_skip_csv)
else:
    print("No matching CSV files found.")

if no_skip_matching_files:
    most_recent_no_skip_csv = max(no_skip_matching_files, key=os.path.getctime)
    df_no_skip = pd.read_csv(most_recent_no_skip_csv)
else:
    print("No matching CSV files without skip found.")


# without skip
df_no_skip = df_no_skip.dropna(subset=['Countdown'])

# Assuming your dataframe is named 'df_no_skip'
df_no_skip.drop(columns=[
    'screenshot',
    'trials.thisRepN',
    'trials.thisTrialN',
    'trials.thisN',
    'trials.thisIndex',
    'trials_6040.thisRepN',
    'trials_6040.thisTrialN',
    'trials_6040.thisN',
    'trials_6040.thisIndex',
    'trials_5743.thisRepN',
    'trials_5743.thisTrialN',
    'trials_5743.thisN',
    'trials_5743.thisIndex',
    'trials_5446.thisRepN',
    'trials_5446.thisTrialN',
    'trials_5446.thisN',
    'trials_5446.thisIndex',
    'trials_5149.thisRepN',
    'trials_5149.thisTrialN',
    'trials_5149.thisN',
    'trials_5149.thisIndex',
    'key_resp_4.started',
    'key_resp_4.keys',
    'key_resp_4.rt',
    'key_resp_2.keys',
    # 'key_resp_2.started',
    'key_resp_3.keys',
    # 'key_resp_2.rt',
    'Videoshowstart',
    'Videoshowstop',
    'date',
    'expName',
    'psychopyVersion',
    'frameRate'
], inplace=True)

replacement_dict = {
        'Countdown_2.5s.mp4': 2.5,
        'Countdown_2s.mp4': 2,
        'Countdown_1.5s.mp4': 1.5
}

# Replace values in the 'Countdown' column
df_no_skip['Countdown'] = df_no_skip['Countdown'].replace(replacement_dict)
df_no_skip.loc[df_no_skip['VideoshowRT'].isna(), 'comb.corr'] = -1
df_no_skip = df_no_skip.dropna(subset=['VideoshowRT'])
# df_no_skip.drop('Left_3.started', axis=1, inplace=True)
# df_no_skip['corr'] = df_no_skip[['response.corr', 'response_2.corr']].sum(axis=1)
try:
    df_no_skip['corr'] = df_no_skip.drop(['response.corr', 'response_2.corr'], axis=1, inplace=True)
except:
    try:    
        df_no_skip['corr'] = df_no_skip.drop(['response_2.corr', 'response_3.corr'], axis=1, inplace=True)
    except:
        try:
            df_no_skip['corr'] = df_no_skip.drop(['response_3.corr', 'response_4.corr'], axis=1, inplace=True)
        except:
            print('')
try:
    df_no_skip['key_skip'] = df_no_skip['key_skip.keys'].combine_first(df_no_skip['key_skip_2.keys'])
except:
    try:    
        df_no_skip['key_skip'] = df_no_skip['key_skip_2.keys'].combine_first(df_no_skip['key_skip_3.keys'])
    except:
        try:
            df_no_skip['key_skip'] = df_no_skip['key_skip_3.keys'].combine_first(df_no_skip['key_skip_4.keys'])
        except:
            print('')
try:
    df_no_skip['response_keys'] = df_no_skip['response.keys'].combine_first(df_no_skip['response_2.keys'])
except:
    try:    
        df_no_skip['response_keys'] = df_no_skip['response_2.keys'].combine_first(df_no_skip['response_3.keys'])   
    except:
        try:
            df_no_skip['response_keys'] = df_no_skip['response_3.keys'].combine_first(df_no_skip['response_4.keys'])
        except:
            print('')
try:
    df_no_skip.drop(['key_skip.keys', 'key_skip_2.keys'], axis=1, inplace=True)
except:
    print("")

    
try:
    df_no_skip['response_keys'] = df_no_skip['response.keys'].combine_first(df_no_skip['response_2.keys'])
    df_no_skip.drop(['response.keys', 'response_2.keys'], axis=1, inplace=True)
except:
    print()
try:
    df_no_skip['response_RT'] = df_no_skip['response.rt'].combine_first(df_no_skip['response_2.rt'])
except:
    try:    
        df_no_skip['response_RT'] = df_no_skip['response_2.rt'].combine_first(df_no_skip['response_3.rt'])
    except:
        try:
            df_no_skip['response_RT'] = df_no_skip['response_3.rt'].combine_first(df_no_skip['response_4.rt'])
        except:
            print('')
try:
    df_no_skip.drop(['response.rt', 'response_2.rt'], axis=1, inplace=True)
except:
    print()

# df_no_skip['skip_RT'] = df_no_skip['key_skip.rt'].combine_first(df_no_skip['key_skip_2.rt'])
# df_no_skip.drop(['key_skip.rt', 'key_skip_2.rt'], axis=1, inplace=True)

df_no_skip = df_no_skip.drop(['text_2.started', 'text_5.started', 'key_resp.started', 'text_9.started', 'key_resp.keys', 'key_resp.rt', 'text_10.started', 'text_10.stopped'], axis=1)
df_no_skip = df_no_skip.drop(['comb.corr'], axis=1)
df_no_skip.loc[(df_no_skip['response_RT'].isna()), 'corr'] = -1


# Optional: Reset the index if desired
df_no_skip = df_no_skip.reset_index(drop=True)
df_no_skip.to_csv('output.csv', index=False)



# with skip
df_skip = df_skip.dropna(subset=['Countdown'])

# Assuming your dataframe is named 'df_skip'
df_skip.drop(columns=[
    'screenshot',
    'trials.thisRepN',
    'trials.thisTrialN',
    'trials.thisN',
    'trials.thisIndex',
    'trials_6040.thisRepN',
    'trials_6040.thisTrialN',
    'trials_6040.thisN',
    'trials_6040.thisIndex',
    'trials_5743.thisRepN',
    'trials_5743.thisTrialN',
    'trials_5743.thisN',
    'trials_5743.thisIndex',
    'trials_5446.thisRepN',
    'trials_5446.thisTrialN',
    'trials_5446.thisN',
    'trials_5446.thisIndex',
    'trials_5149.thisRepN',
    'trials_5149.thisTrialN',
    'trials_5149.thisN',
    'trials_5149.thisIndex',
    'key_resp_4.started',
    'key_resp_4.keys',
    'key_resp_4.rt',
    'key_resp_2.keys',
    'key_resp_3.started',
    'key_resp_3.keys',
    'key_resp_3.rt',
    'Videoshowstart',
    'Videoshowstop',
    'date',
    'expName',
    'psychopyVersion',
    'frameRate'
], inplace=True)

replacement_dict = {
        'Countdown_2.5s.mp4': 2.5,
        'Countdown_2s.mp4': 2,
        'Countdown_1.5s.mp4': 1.5
}

# Replace values in the 'Countdown' column
df_skip['Countdown'] = df_skip['Countdown'].replace(replacement_dict)
df_skip.loc[df_skip['VideoshowRT'].isna(), 'comb.corr'] = -1
df_skip = df_skip.dropna(subset=['VideoshowRT'])
# df_skip.drop('Left_3.started', axis=1, inplace=True)
# df_skip['corr'] = df_skip[['response.corr', 'response_2.corr']].sum(axis=1)
try:
    df_skip['corr'] = df_skip.drop(['response.corr', 'response_2.corr'], axis=1, inplace=True)
except:
    try:    
        df_skip['corr'] = df_skip.drop(['response_2.corr', 'response_3.corr'], axis=1, inplace=True)
    except:
        try:
            df_skip['corr'] = df_skip.drop(['response_3.corr', 'response_4.corr'], axis=1, inplace=True)
        except:
            print('')
try:
    df_skip['key_skip'] = df_skip['key_skip.keys'].combine_first(df_skip['key_skip_2.keys'])
except:
    try:    
        df_skip['key_skip'] = df_skip['key_skip_2.keys'].combine_first(df_skip['key_skip_3.keys'])
    except:
        try:
            df_skip['key_skip'] = df_skip['key_skip_3.keys'].combine_first(df_skip['key_skip_4.keys'])
        except:
            print('')
try:
    df_skip['response_keys'] = df_skip['response.keys'].combine_first(df_skip['response_2.keys'])
except:
    try:    
        df_skip['response_keys'] = df_skip['response_2.keys'].combine_first(df_skip['response_3.keys'])   
    except:
        try:
            df_skip['response_keys'] = df_skip['response_3.keys'].combine_first(df_skip['response_4.keys'])
        except:
            print('')
try:
    df_skip.drop(['key_skip.keys', 'key_skip_2.keys'], axis=1, inplace=True)
except:
    print("")

    
try:
    df_skip['response_keys'] = df_skip['response.keys'].combine_first(df_skip['response_2.keys'])
    df_skip.drop(['response.keys', 'response_2.keys'], axis=1, inplace=True)
except:
    print()
try:
    df_skip['response_RT'] = df_skip['response.rt'].combine_first(df_skip['response_2.rt'])
except:
    try:    
        df_skip['response_RT'] = df_skip['response_2.rt'].combine_first(df_skip['response_3.rt'])
    except:
        try:
            df_skip['response_RT'] = df_skip['response_3.rt'].combine_first(df_skip['response_4.rt'])
        except:
            print('')
try:
    df_skip.drop(['response.rt', 'response_2.rt'], axis=1, inplace=True)
except:
    print()

# df_skip['skip_RT'] = df_skip['key_skip.rt'].combine_first(df_skip['key_skip_2.rt'])
# df_skip.drop(['key_skip.rt', 'key_skip_2.rt'], axis=1, inplace=True)
try:
    df_skip = df_skip.drop(['text_2.started', 'text_5.started', 'key_resp.started', 'text_9.started', 'key_resp.keys', 'key_resp.rt', 'text_10.started', 'text_10.stopped'], axis=1)
except:
    print()
df_skip = df_skip.drop(['comb.corr'], axis=1)
df_skip.loc[(df_skip['response_RT'].isna()), 'corr'] = -1


# Optional: Reset the index if desired
df_skip = df_skip.reset_index(drop=True)
df_skip.to_csv('output2.csv', index=False)

df_total = pd.read_csv('df_total.csv')


df_data = pd.read_csv('output.csv')
df_data2 = pd.read_csv('output2.csv')
df_data_concat = pd.concat([df_data, df_data2])
df_data_concat.reset_index(drop=True, inplace=True)
add_row = [df_data.loc[1, 'participant'], df_data.loc[1, 'Dot Ratio'], df_data.loc[1, 'Deadline'],df_data_concat.loc[:, 'VideoshowRT'].mean(),df_data_concat.loc[:239, 'VideoshowRT'].mean(),df_data.query("corr == 1")['VideoshowRT'].mean(),df_data.query("corr == 0")['VideoshowRT'].mean(),df_data_concat.loc[:240, 'VideoshowRT'].mean(), df_data2.query("key_skip != 'space'")['VideoshowRT'].mean(),df_data2.query("corr == 1")['VideoshowRT'].mean(),df_data2.query("corr == 0")['VideoshowRT'].mean(),df_data['total_score'].iloc[-1], df_data2['total_score'].iloc[-1], len(df_data),len(df_data2), len(df_data.query("corr == 1"))/len(df_data) , len(df_data2.query("corr == 1"))/len(df_data2), len(df_data.query("`corr` == -1")), len(df_data2.query("`corr` == -1")) ,len(df_data.query("`response_keys` == 'None'")), len(df_data2.query("`response_keys` == 'None' and `key_skip` == 'None'")), len(df_data2.query("`key_skip` != 'None'")),df_data['total_score'].iloc[-1]/(len(df_data)), df_data2['total_score'].iloc[-1]/(len(df_data2)), df_data2['total_score'].iloc[-1]/(len(df_data2.query("`key_skip` == 'None'")))]
# add_row =                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     []
df_total.loc[len(df_total)] = add_row

import os

file_path = 'output.csv'  # Replace with the actual path of the file you want to delete
file_path2 = 'output2.csv'  # Replace with the actual path of the file you want to delete

try:
    os.remove(file_path)
    os.remove(file_path2)

    print(f"The file '{file_path}' has been deleted successfully.")
    print(f"The file '{file_path2}' has been deleted successfully.")

except OSError as e:
    print(f"Error occurred while deleting the file: {e}")
csv_file_path = 'df_total.csv'  # Replace with the desired file path and name
df_total.to_csv(csv_file_path, index=False)