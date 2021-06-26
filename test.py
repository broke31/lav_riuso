import os

import pandas as pd
from FileSystem import get_sub_dir

project = "junit/"
base_folder = "/home/broke31/Desktop/test/proj/" + project
my_unique = "/home/broke31/Desktop/test/smell_an_unique/" + project

if not os.path.exists(my_unique):
    os.makedirs(my_unique)

list_folder = get_sub_dir(base_folder)
base_line = "junit-3.7"
i = 0
list_df_isClassDataShouldBePrivate = []
list_df_isComplexClass = []
list_df_isFunctionalDecomposition = []
list_df_isGodClass = []
list_df_isSpaghettiCode = []
print(len(list_folder))
for sub_dir in list_folder:
    base_folder_sub_dir = base_folder + sub_dir
    list_df_isClassDataShouldBePrivate.append(pd.read_csv(base_folder_sub_dir + "/isClassDataShouldBePrivate.csv"))
    list_df_isComplexClass.append(pd.read_csv(base_folder_sub_dir + "/isComplexClass.csv"))
    list_df_isFunctionalDecomposition.append(pd.read_csv(base_folder_sub_dir + "/isFunctionalDecomposition.csv"))
    list_df_isGodClass.append(pd.read_csv(base_folder_sub_dir + "/isGodClass.csv"))
    list_df_isSpaghettiCode.append(pd.read_csv(base_folder_sub_dir + "/isSpaghettiCode.csv"))

df_concat_isClassDataShouldBePrivate = pd.concat(list_df_isClassDataShouldBePrivate)
df_is_ClassDataShouldBePrivate = df_concat_isClassDataShouldBePrivate[df_concat_isClassDataShouldBePrivate.
                                                                          groupby('Class Name')['Class Name'].transform(
    'size') == len(
    list_folder)]

df_is_ClassDataShouldBePrivate = df_is_ClassDataShouldBePrivate.sort_values('Class Name').drop_duplicates(
    subset=['Class Name', 'Release'], keep='last')

df_concat_is_complex_class = pd.concat(list_df_isComplexClass)
df_is_complex_class = df_concat_is_complex_class[df_concat_is_complex_class.
                                                     groupby('Class Name')['Class Name'].transform(
    'size') == len(
    list_folder)]

df_is_complex_class = df_is_complex_class.sort_values('Class Name').drop_duplicates(
    subset=['Class Name', 'Release'], keep='last')

df_concat_is_functional_dec = pd.concat(list_df_isFunctionalDecomposition)
df_is_functional_dec = df_concat_is_functional_dec[df_concat_is_functional_dec.
                                                       groupby('Class Name')['Class Name'].transform(
    'size') == len(
    list_folder)]

df_is_functional_dec = df_is_functional_dec.sort_values('Class Name').drop_duplicates(
    subset=['Class Name', 'Release'], keep='last')

df_concat_isGodClass = pd.concat(list_df_isGodClass)
df_is_god_class = df_concat_isGodClass[df_concat_isGodClass.
                                           groupby('Class Name')['Class Name'].transform(
    'size') == len(
    list_folder)]

df_is_god_class = df_is_god_class.sort_values('Class Name').drop_duplicates(
    subset=['Class Name', 'Release'], keep='last')

df_concat_isSpaghetti = pd.concat(list_df_isSpaghettiCode)
df_is_spaghetti = df_concat_isSpaghetti[df_concat_isSpaghetti.
                                            groupby('Class Name')['Class Name'].transform(
    'size') == len(
    list_folder)]

df_is_spaghetti = df_is_spaghetti.sort_values('Class Name').drop_duplicates(
    subset=['Class Name', 'Release'], keep='last')

df_is_ClassDataShouldBePrivate.to_csv(my_unique + "is_class_should_be_private.csv", index=False)
df_is_complex_class.to_csv(my_unique + "is_complex_data.csv", index=False)
df_is_functional_dec.to_csv(my_unique + "is_functional_dec.csv", index=False)
df_is_god_class.to_csv(my_unique + "is_god_class.csv", index=False)
df_is_spaghetti.to_csv(my_unique + "is_spaghetti.csv", index=False)
