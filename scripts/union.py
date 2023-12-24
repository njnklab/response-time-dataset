'''
将生成的数据集保留交集
'''

import pandas as pd
import os

def get_common_export_ids(path):
    # list all csv files
    csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
    if not csv_files:
        print("No CSV files found in the specified path.")
        return
    
    # initialize common_export_ids
    common_export_ids = set()

    # begin with the first file
    df_first = pd.read_csv(os.path.join(path, csv_files[0]))
    common_export_ids = set(df_first['export_id'])
    
    # find common export_ids
    for file in csv_files[1:]:
        df = pd.read_csv(os.path.join(path, file))
        current_export_ids = set(df['export_id'])
        common_export_ids.intersection_update(current_export_ids)

    return common_export_ids

def filter_and_save_csvs(path, common_export_ids):
    csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
    for file in csv_files:
        file_path = os.path.join(path, file)
        df = pd.read_csv(file_path)
        filtered_df = df[df['export_id'].isin(common_export_ids)]
        filtered_df.to_csv(file_path, index=False)

def main():
    path = '/home/ubuntu/proj/rt-dataset/src/data/'
    common_export_ids = get_common_export_ids(path)
    if common_export_ids:
        filter_and_save_csvs(path, common_export_ids)
        print("CSV files have been modified!")
    else:
        print("No common export_ids found across the files.")

if __name__ == "__main__":
    main()
