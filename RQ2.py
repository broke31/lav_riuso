import os
from os.path import join

import pandas as pd

from FileSystem import get_sub_dir
from Reformat import reformat_ant


def min_max(x):
    return (x - min(x)) / (max(x) - min(x))


name_folder = "ant"

path_to_rq2 = "/home/broke31/Desktop/Lav_riuso/RQ2/" + name_folder + "/"
path_to_ris_rq2 = "/home/broke31/Desktop/Lav_riuso/ris_RQ2/" + name_folder + "/"
path_proj_th = "/home/broke31/Desktop/Lav_riuso/smell_an_unique/" + name_folder + "/"
smell = "is_god_class"
m = "LCOM2"
m1 = "featureSum"
m2 = "ELOC"
if not os.path.exists(path_to_rq2):
    os.makedirs(path_to_rq2)

if not os.path.exists(path_to_ris_rq2):
    os.makedirs(path_to_ris_rq2)

list_sub_folder = get_sub_dir(path=path_to_rq2)

class_name = "Nome del tipo"
for sub_folder in list_sub_folder:
    df_to_save = pd.DataFrame()
    l = sub_folder.split("-")
    current_release = l[0]
    next_release = l[1]
    current_release_csv = pd.read_csv(path_to_rq2 + sub_folder + "/" + current_release + ".csv")
    next_release_csv = pd.read_csv(path_to_rq2 + sub_folder + "/" + next_release + ".csv")
    current_release_csv_sorted = current_release_csv.sort_values(class_name)
    next_release_csv_sorted = next_release_csv.sort_values(class_name)
    current_release_csv_sorted = current_release_csv_sorted.reset_index(drop=True)
    next_release_csv_sorted = next_release_csv_sorted.reset_index(drop=True)
    df_to_save[next_release + "-" + current_release] = current_release_csv_sorted[class_name]
    metric_list = ["DIT", "WMC", "NOC", "LCOM", "CBO", "RFC", "NOM",
                   "NA", "Delegation", "Delegation2", "Inh_impl", "nMO",
                   "Inh_spec", "LOC", "NORM", "NSF", "NSM", "SIX"]
    for metric in metric_list:
        df_to_save[metric + " " + current_release] = current_release_csv_sorted[metric]
        df_to_save[metric + " " + next_release] = next_release_csv_sorted[metric]
        df_to_save[metric + "-sub"] = next_release_csv_sorted[metric] - current_release_csv_sorted[metric]

    df_th_should_be_private = pd.read_csv(path_proj_th + smell + ".csv")
    df_th_should_be_private_reformatted = reformat_ant(df_th_should_be_private)
    df_th_current_release_sh_be_pr = df_th_should_be_private_reformatted[
        df_th_should_be_private_reformatted["Release"] == current_release]
    df_th_next_release_sh_be_pr = df_th_should_be_private_reformatted[
        df_th_should_be_private_reformatted["Release"] == next_release]
    inte = next_release + "-" + current_release
    df_to_save = df_to_save.reset_index(drop=True)
    df_th_current_release_sh_be_pr = df_th_current_release_sh_be_pr.reset_index(drop=True)
    df_th_next_release_sh_be_pr = df_th_next_release_sh_be_pr.reset_index(drop=True)
    # mergedStuff = pd.merge(df1, df2, on=['Name'], how='inner')
    # s1 = pd.merge(df_to_save, df_th_current_release_sh_be_pr, how='inner', on=[next_release +"-"+current_release,'Release'])
    list_class_current_release_sh_be_pr_th = list(df_th_current_release_sh_be_pr["Class Name"])

    df_to_save_new = df_to_save[df_to_save[inte].isin(list_class_current_release_sh_be_pr_th)]
    df_to_save_new = df_to_save_new.reset_index(drop=True)
    df_th_current_release_sh_be_pr = df_th_current_release_sh_be_pr.reset_index(drop=True)

    df_to_save_new[m + current_release] = min_max(df_th_current_release_sh_be_pr[m])
    print(df_to_save_new[m+current_release])
    df_to_save_new[m + next_release] = min_max(df_th_next_release_sh_be_pr[m])
    df_to_save_new[m1 + current_release] = min_max(df_th_current_release_sh_be_pr[m1])
    df_to_save_new[m1 + next_release] = min_max(df_th_next_release_sh_be_pr[m1])

    df_to_save_new[m2 + current_release] = min_max(df_th_current_release_sh_be_pr[m2])
    df_to_save_new[m2 + next_release] = min_max(df_th_next_release_sh_be_pr[m2])

    df_smelliness = pd.DataFrame()
    df_smelliness['0'] = df_to_save_new[m + current_release]
    df_smelliness['1'] = df_to_save_new[m + next_release]
    df_smelliness['2'] = df_to_save_new[m1 + current_release]
    df_smelliness['3'] = df_to_save_new[m1 + next_release]
    df_smelliness['4'] = df_to_save_new[m2 + current_release]
    df_smelliness['5'] = df_to_save_new[m2 + next_release]
    print(df_smelliness)

    df_to_save_new['Smelliness'] = df_smelliness.mean(axis=1)

    print(df_to_save)
    print(df_to_save_new)

    df_to_save.reset_index(drop=True)
    df_th_current_release_sh_be_pr = df_th_current_release_sh_be_pr.reset_index(drop=True)
    df_th_next_release_sh_be_pr = df_th_next_release_sh_be_pr.reset_index(drop=True)

    df_to_save_new.to_csv(path_to_ris_rq2 + inte + smell + ".csv", index=False)
