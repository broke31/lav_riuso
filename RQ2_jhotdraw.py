import os
from os.path import join

import pandas as pd

from FileSystem import get_sub_dir
from Reformat import reformat_ant, reformatted_jedit, reformatted_jhotdraw


def min_max(x):
    return (x - min(x)) / (max(x) - min(x))


name_folder = "jhotdraw"

path_to_rq2 = "/home/broke31/Desktop/Lav_riuso/RQ2/" + name_folder + "/"
path_to_ris_rq2 = "/home/broke31/Desktop/Lav_riuso/ris_RQ2/" + name_folder + "/"
path_proj_th = "/home/broke31/Desktop/Lav_riuso/smell_an_unique/" + name_folder + "/"
smell = "is_spaghetti"
m = "ELOC"
#m1 = "featureSum"
#m2 = "ELOC"
if not os.path.exists(path_to_rq2):
    os.makedirs(path_to_rq2)

if not os.path.exists(path_to_ris_rq2):
    os.makedirs(path_to_ris_rq2)

list_sub_folder = get_sub_dir(path=path_to_rq2)
class_name = "Nome del tipo"
for sub_folder in list_sub_folder:
    df_to_save = pd.DataFrame()
    get_versions = sub_folder.split("-")
    current_version = get_versions[0]
    next_version = get_versions[1]
    current_version_CSV = pd.read_csv(path_to_rq2 + sub_folder + "/" + current_version + ".csv")
    next_version_CSV = pd.read_csv(path_to_rq2 + sub_folder + "/" + next_version + ".csv")
    current_version_CSV_ord = current_version_CSV.sort_values(class_name)
    next_version_CSV_ord = next_version_CSV.sort_values(class_name)
    current_version_CSV_ord_res = current_version_CSV_ord.reset_index(drop=True)
    next_version_CSV_ord_res = next_version_CSV_ord.reset_index(drop=True)
    df_to_save[current_version + "-" + next_version] = current_version_CSV_ord_res[class_name]
    metric_list = ["DIT", "WMC", "NOC", "LCOM", "CBO", "RFC", "NOM",
                   "NA", "Delegation", "Delegation2", "Inh_impl", "nMO",
                   "Inh_spec", "LOC", "NORM", "NSF", "NSM", "SIX"]
    for metric in metric_list:
        df_to_save[metric + " " + current_version] = current_version_CSV_ord_res[metric]
        df_to_save[metric + " " + next_version] = next_version_CSV_ord_res[metric]
        df_to_save[metric + "-sub"] = current_version_CSV_ord_res[metric] - next_version_CSV_ord_res[metric]
    df_th = pd.read_csv(path_proj_th + smell + ".csv")
    print(df_th)
    df_th_reformatted = reformatted_jhotdraw(df_th)
    print(df_to_save)
    print(df_th_reformatted)

    df_th_current_release_ref = df_th_reformatted[
        df_th_reformatted["Release"] == current_version]
    df_th_next_release_ref = df_th_reformatted[
        df_th_reformatted["Release"] == next_version]
    inte = current_version + "-" + next_version
    print(df_th_current_release_ref)
    list_class_name = list(df_th_current_release_ref["Class Name"])
    print(df_to_save)

    df_to_save_new = df_to_save[df_to_save[inte].isin(list_class_name)]
    print(list_class_name)
    df_to_save_new = df_to_save_new.reset_index(drop=True)
    df_th_current_release_ref = df_th_current_release_ref.reset_index(drop=True)
    df_th_next_release_ref = df_th_next_release_ref.reset_index(drop=True)
    print(df_to_save_new)
    #### add metrics
    df_th_current_release_ref = df_th_current_release_ref.reset_index(drop=True)
    df_th_next_release_ref = df_th_next_release_ref.reset_index(drop=True)
    df_to_save_new = df_to_save_new.reset_index(drop=True)
    df_to_save = df_to_save.reset_index(drop=True)

    df_to_save_new[m + current_version] = min_max(df_th_current_release_ref[m])
    df_to_save_new[m + next_version] = min_max(df_th_next_release_ref[m])
    print(df_to_save_new)

    df_th_current_release_ref = df_th_current_release_ref.reset_index(drop=True)
    df_th_next_release_ref = df_th_next_release_ref.reset_index(drop=True)
    df_to_save_new = df_to_save_new.reset_index(drop=True)
    df_to_save = df_to_save.reset_index(drop=True)

    #  df_to_save_new[m1 + current_version] = min_max(df_th_current_release_ref[m1])
    # df_to_save_new[m1 + next_version] = min_max(df_th_current_release_ref[m1])
    print(df_to_save_new)

    df_th_current_release_ref = df_th_current_release_ref.reset_index(drop=True)
    df_th_next_release_ref = df_th_next_release_ref.reset_index(drop=True)
    df_to_save_new = df_to_save_new.reset_index(drop=True)
    df_to_save = df_to_save.reset_index(drop=True)

  #  df_to_save_new[m2 + current_version] = min_max(df_th_current_release_ref[m2])
    #  df_to_save_new[m2 + next_version] = min_max(df_th_next_release_ref[m2])

    df_th_current_release_ref = df_th_current_release_ref.reset_index(drop=True)
    df_th_next_release_ref = df_th_next_release_ref.reset_index(drop=True)
    df_to_save_new = df_to_save_new.reset_index(drop=True)
    df_to_save = df_to_save.reset_index(drop=True)
    df_to_save_new_with_fill_na = df_to_save_new.fillna(0)

    df_smelliness = pd.DataFrame()
    df_smelliness['0'] = df_to_save_new[m + current_version]
    df_smelliness['1'] = df_to_save_new[m + next_version]
    # df_smelliness['2'] = df_to_save_new[m1 + current_version]
    # df_smelliness['3'] = df_to_save_new[m1 + next_version]
    # df_smelliness['4'] = df_to_save_new[m2 + current_version]
    # df_smelliness['5'] = df_to_save_new[m2 + next_version]

    df_smelliness_fill_na = df_smelliness.fillna(0)
    df_to_save_new_with_fill_na['Smelliness'] = df_smelliness_fill_na.mean(axis=1)
    df_to_save_new_with_fill_na.to_csv(path_to_ris_rq2 + inte + smell + ".csv", index=False)








