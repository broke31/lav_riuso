import pandas as pd
import os
from natsort import natsorted

import MergeCSV
from FileSystem import get_list_file_csv

name_folder = "junit"
base_folder = "/home/broke31/Desktop/code_smell_an/projects_csv_rev6"
path_to_save = "/home/broke31/Desktop/Lav_riuso/uniqueRQ1_sesa/" + name_folder + "/"
path_ans_rq1 = "/home/broke31/Desktop/Lav_riuso/ans_RQ1_sesa/" + name_folder + "/"
path_to_rq2 = "/home/broke31/Desktop/Lav_riuso/RQ1_sesa/" + name_folder + "/"

if not os.path.exists(path_to_save):
    os.makedirs(path_to_save)

if not os.path.exists(path_ans_rq1):
    os.makedirs(path_ans_rq1)

if not os.path.exists(path_to_rq2):
    os.makedirs(path_to_rq2)

list_file_folder = get_list_file_csv(base_folder)
base_version = "junit-3.7"

merged_csv = MergeCSV.merge_csv(base_folder)
base_csv = merged_csv.loc[merged_csv['Nome del progetto'] == base_version]
version_name = "Nome del progetto"
class_name = "Nome del tipo"
list_class_name_base_csv = list(base_csv[class_name])
first_filter = merged_csv[merged_csv[class_name].isin(list_class_name_base_csv)]
list_dataframes = [first_filter]
df_concat_ = pd.concat(list_dataframes)
df_second_filter = df_concat_[df_concat_.groupby(class_name)[class_name].transform('size') > len(
    list_file_folder) - 1]
final = df_second_filter.drop_duplicates([version_name, class_name], keep='last')
final.insert(0, 'Project', name_folder)
list_value_version = final[version_name].unique()
sorted_list_file = natsorted(list_value_version)
for i in range(0, len(sorted_list_file) - 1):
    path_to_rq2 = "/home/broke31/Desktop/Lav_riuso/RQ2/" + name_folder + "/"
    df_to_save_Inh_impl = pd.DataFrame()
    current_release = final.loc[final[version_name] == sorted_list_file[i]]
    next_release = final.loc[final[version_name] == sorted_list_file[i + 1]]
    sorted_current_release = current_release.sort_values(class_name)
    sorted_next_release = next_release.sort_values(class_name)
    df_to_save_Inh_impl["class name"] = sorted_current_release[class_name]
    df_to_save_Inh_impl = df_to_save_Inh_impl.reset_index(drop=True)
    sorted_current_release = sorted_current_release.reset_index(drop=True)
    sorted_next_release = sorted_next_release.reset_index(drop=True)
    df_to_save_Inh_impl[sorted_list_file[i]] = sorted_current_release['Inh_impl'] / sorted_current_release["LOC"]
    df_to_save_Inh_impl[sorted_list_file[i + 1]] = sorted_next_release['Inh_impl'] / sorted_next_release["LOC"]
    subdir = sorted_list_file[i] + "-" + sorted_list_file[i + 1]
    subdir_complete = path_ans_rq1 + "/" + subdir
    if not os.path.exists(subdir_complete):
        os.makedirs(subdir_complete)
    df_to_save_Inh_impl.to_csv(subdir_complete + "/inh_imp.csv", index=False)

    df_to_save_Inh_spec = pd.DataFrame()
    df_to_save_Inh_spec["class name"] = sorted_current_release[class_name]
    df_to_save_Inh_spec = df_to_save_Inh_spec.reset_index(drop=True)
    df_to_save_Inh_spec[sorted_list_file[i]] = sorted_current_release['Inh_spec'] / sorted_current_release["LOC"]
    df_to_save_Inh_spec[sorted_list_file[i + 1]] = sorted_next_release['Inh_spec'] / sorted_next_release["LOC"]
    df_to_save_Inh_spec.to_csv(subdir_complete + "/Inh_spec.csv", index=False)

    df_to_save_delegation = pd.DataFrame()
    df_to_save_delegation["class name"] = sorted_current_release[class_name]
    df_to_save_delegation = df_to_save_delegation.reset_index(drop=True)
    df_to_save_delegation[sorted_list_file[i]] = sorted_current_release['Delegation2'] / sorted_current_release["LOC"]
    df_to_save_delegation[sorted_list_file[i + 1]] = sorted_next_release['Delegation2'] / sorted_next_release["LOC"]
    df_to_save_delegation.to_csv(subdir_complete + "/Delegation2.csv", index=False)

    ####################################### Generate folder for RQ2##############
    path_to_rq2 = path_to_rq2 + subdir
    print(path_to_rq2)
    if not os.path.exists(path_to_rq2):
        os.makedirs(path_to_rq2)
    sorted_current_release.to_csv(path_to_rq2 + "/" + sorted_list_file[i] + ".csv", index=False)
    sorted_next_release.to_csv(path_to_rq2 + "/" + sorted_list_file[i + 1] + ".csv", index=False)

final.to_csv(path_to_save + "/" + name_folder + "_unique.csv", index=False)
base_csv = final.loc[final[version_name] == base_version]
base_csv.to_csv(path_to_save + "/" + name_folder + "_baseline.csv", index=False)
