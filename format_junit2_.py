import os

import pandas as pd

base_path = "/home/broke31/Desktop/test/smell_an_unique/junit"

current_rel = "junit-4.6"
next_rel = "junit-4.7"

list_smells = ["is_class_should_be_private", "is_complex_data",
               "is_functional_dec", "is_god_class",
               "is_spaghetti"
               ]

is_class = pd.read_csv(base_path + "/" + list_smells[0] + ".csv")
is_complex = pd.read_csv(base_path + "/" + list_smells[1] + ".csv")
is_functional_dec = pd.read_csv(base_path + "/" + list_smells[2] + ".csv")
is_god_class = pd.read_csv(base_path + "/" + list_smells[3] + ".csv")
is_spaghetti = pd.read_csv(base_path + "/" + list_smells[4] + ".csv")

list_csv = [is_class, is_complex, is_functional_dec,
            is_god_class, is_spaghetti
            ]
name_version_to_salve = current_rel + "-" + next_rel

df_current_is_class = is_class[is_class["Release"] == current_rel]
df_current_is_complex = is_complex[is_complex["Release"] == current_rel]
df_current_is_functional = is_functional_dec[is_functional_dec["Release"] == current_rel]
df_current_god_class = is_god_class[is_god_class["Release"] == current_rel]
df_current_is_spaghetti_ = is_spaghetti[is_spaghetti["Release"] == current_rel]

df_current_is_class = df_current_is_class.sort_values(by=["Class Name"])
df_current_is_complex = df_current_is_complex.sort_values(by=["Class Name"])
df_current_is_functional = df_current_is_functional.sort_values(by=["Class Name"])
df_current_god_class = df_current_god_class.sort_values(by=["Class Name"])
df_current_is_spaghetti_ = df_current_is_spaghetti_.sort_values(by=["Class Name"])

df_next_is_class = is_class[is_class["Release"] == next_rel]
df_next_is_complex = is_complex[is_complex["Release"] == next_rel]
df_next_is_functional = is_functional_dec[is_functional_dec["Release"] == next_rel]
df_next_god_class = is_god_class[is_god_class["Release"] == next_rel]
df_next_is_spaghetti_ = is_spaghetti[is_spaghetti["Release"] == next_rel]

df_next_is_class = df_next_is_class.sort_values(by=["Class Name"])
df_next_is_complex = df_next_is_complex.sort_values(by=["Class Name"])
df_next_is_functional = df_next_is_functional.sort_values(by=["Class Name"])
df_next_god_class = df_next_god_class.sort_values(by=["Class Name"])
df_next_is_spaghetti_ = df_next_is_spaghetti_.sort_values(by=["Class Name"])

to_save_current_version = pd.DataFrame()
to_save_next_version = pd.DataFrame()

to_save_current_version["Project"] = df_current_is_complex["Project"]
to_save_current_version["Release"] = df_current_is_complex["Release"]
to_save_current_version["Class Name"] = df_current_is_complex["Class Name"]
to_save_current_version["NOPA"] = df_current_is_class["NOPA"]
to_save_current_version["mcCabeMetric"] = df_current_is_complex["mcCabeMetric"]
to_save_current_version["WCM"] = df_current_is_functional["WCM"]
to_save_current_version["LCOM2"] = df_current_god_class["LCOM2"]
to_save_current_version["featureSum"] = df_current_god_class["featureSum"]
to_save_current_version["ELOC"] = df_current_god_class["ELOC"]
to_save_current_version["DIT"] = df_current_is_complex["DIT"]
to_save_current_version["NOC"] = df_current_is_complex["NOC"]
to_save_current_version["LOC"] = df_current_is_complex["LOC"]




to_save_next_version["Project"] = df_next_is_complex["Project"]
to_save_next_version["Release"] = df_next_is_complex["Release"]
to_save_next_version["Class Name"] = df_next_is_complex["Class Name"]
to_save_next_version["NOPA"] = df_next_is_class["NOPA"]
to_save_next_version["mcCabeMetric"] = df_next_is_complex["mcCabeMetric"]
to_save_next_version["WCM"] = df_next_is_functional["WCM"]
to_save_next_version["LCOM2"] = df_next_god_class["LCOM2"]
to_save_next_version["featureSum"] = df_next_god_class["featureSum"]
to_save_next_version["ELOC"] = df_next_god_class["ELOC"]
to_save_next_version["DIT"] = df_next_is_complex["DIT"]
to_save_next_version["NOC"] = df_next_is_complex["NOC"]
to_save_next_version["LOC"] = df_next_is_complex["LOC"]

path_to_save = "/home/broke31/Desktop/test/junit_new/"
if not os.path.exists(path_to_save):
    os.makedirs(path_to_save)

to_save_current_version.to_csv(path_to_save+current_rel+".csv",index=False)
to_save_next_version.to_csv(path_to_save+next_rel+".csv",index=False)


