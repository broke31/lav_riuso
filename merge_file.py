import os

import pandas as pd

from FileSystem import get_sub_dir, get_list_file_csv, get_version_from_file


def add_labels(row):
    print(row)
    if row['Smelliness'] > 0:
        return 'Increase'
    if row['Smelliness'] < 0:
        return 'Decrease'
    if row['Smelliness'] == 0:
        return 'Stable'


base_folder = "/home/broke31/Desktop/Lav_riuso/ris_RQ2/"
folders = get_sub_dir(base_folder)

for folder in folders:
    list_folder_smell = get_sub_dir(base_folder + folder)
    df = pd.DataFrame()
    for folder_smell in list_folder_smell:
        print(folder_smell)
        path_sub_folder = base_folder + folder + "/" + folder_smell
        csv_path = get_list_file_csv(path_sub_folder)
        for file in csv_path:
            folder_RQ2_with_proj_ = "/home/broke31/Desktop/Lav_riuso/RQ2_with_proj/"
            version = get_version_from_file(file, folder_smell)
            file_csv = pd.read_csv(file)
            print(file_csv)
            file_csv["Version"] = version
            file_csv["Project"] = folder
            file_csv['Smelliness_label_' + version] = file_csv.apply(add_labels, axis=1)
            file_csv.rename(columns={'Smelliness': "Smellinesss_"+version}, inplace=True)
            first_column = file_csv.pop('Project')
            second_row = file_csv.pop("Version")
            file_csv.insert(0, 'Project', first_column)
            file_csv.insert(1, 'Version', second_row)
            print(file_csv)
            folder_RQ2_with_proj_ = folder_RQ2_with_proj_+ folder + "/"+ version +"/"+folder_smell+"/"
            print(folder_RQ2_with_proj_)
            if not os.path.exists(folder_RQ2_with_proj_):
                os.makedirs(folder_RQ2_with_proj_)
            file_csv.to_csv(folder_RQ2_with_proj_+version+"_"+folder_smell+".csv",index = False)