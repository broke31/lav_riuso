import pandas as pd
import os
from pathlib import Path


def get_list_file_csv(base):
    result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(base) for f in filenames if
              os.path.splitext(f)[1] == '.csv']
    return result


def intersection(lst1, lst2):
    return set(lst1).intersection(lst2)


def get_parent(pth, back=2):
    path_second_folder = Path(pth)
    list_elements_path_second_folder = path_second_folder.parts
    size = len(list_elements_path_second_folder)
    return list_elements_path_second_folder[size - back]


def get_name_file_from_path(path, ext=False):
    path_list = path.split(os.sep)
    l = len(path_list)
    to_return = ""
    name_file = path_list[l - 1]
    if not ext:
        to_return = name_file.rsplit('.', 1)[0]  # remove ext
    return to_return



name_folder = "junit"
first_folder = "/home/broke31/Desktop/test/" + name_folder + "/junit-4.6/"
second_folder = "/home/broke31/Desktop/test/" + name_folder + "/junit-4.7/"
print(first_folder)
list_file_first_folder = get_list_file_csv(first_folder)
print(list_file_first_folder)
list_file_second_folder = get_list_file_csv(second_folder)
is_spaghetti_code_first_csv = None
is_god_class_first_csv = None
is_functional_decomposition_first_csv = None
is_class_data_should_be_private_first_csv = None
is_complex_class_first_dir = None
isMiddleMan_first_dir_csv = None
isRefusedBequest_first_dir_csv = None

for complete_file_name in list_file_first_folder:
    name_file = get_name_file_from_path(complete_file_name)
    print(name_file)
    if name_file == "isSpaghettiCode":
        is_spaghetti_code_first_csv = pd.read_csv(complete_file_name)
    if name_file == "isGodClass":
        is_god_class_first_csv = pd.read_csv(complete_file_name)

    if name_file == "isFunctionalDecomposition":
        is_functional_decomposition_first_csv = pd.read_csv(complete_file_name)

    if name_file == "isClassDataShouldBePrivate":
        is_class_data_should_be_private_first_csv = pd.read_csv(complete_file_name)
    if name_file == "isComplexClass":
        is_complex_class_first_dir = pd.read_csv(complete_file_name)
    if name_file == "isMiddleMan":
        isMiddleMan_first_dir_csv = pd.read_csv(complete_file_name)
    if name_file == "isRefusedBequest":
        isRefusedBequest_first_dir_csv = pd.read_csv(complete_file_name)

is_spaghetti_code_second_csv = None
is_god_class_second_csv = None
is_functional_decomposition_second_csv = None
is_class_data_should_be_private_second_csv = None
is_complex_second_csv = None
isMiddleMan_second_dir_csv = None
isRefusedBequest_second_dir_csv = None

for complete_file_name in list_file_second_folder:
    name_file = get_name_file_from_path(complete_file_name)
    if name_file == "isSpaghettiCode":
        is_spaghetti_code_second_csv = pd.read_csv(complete_file_name)
    if name_file == "isGodClass":
        is_god_class_second_csv = pd.read_csv(complete_file_name)

    if name_file == "isFunctionalDecomposition":
        is_functional_decomposition_second_csv = pd.read_csv(complete_file_name)

    if name_file == "isClassDataShouldBePrivate":
        is_class_data_should_be_private_second_csv = pd.read_csv(complete_file_name)
    if name_file == "isComplexClass":
        is_complex_class_second_csv = pd.read_csv(complete_file_name)

    if name_file == "isMiddleMan":
        isMiddleMan_second_dir_csv = pd.read_csv(complete_file_name)
    if name_file == "isRefusedBequest":
        isRefusedBequest_second_dir_csv = pd.read_csv(complete_file_name)

dict_current_version = {
    "isSpaghettiCode": is_spaghetti_code_first_csv,
    "isGodClass": is_god_class_first_csv,
    "isFunctionalDecomposition": is_functional_decomposition_first_csv,
    "isClassDataShouldBePrivate": is_class_data_should_be_private_first_csv,
    "isComplexClass": is_complex_class_first_dir,
    "isMiddleMan": isMiddleMan_first_dir_csv,
    "isRefusedBequest": isRefusedBequest_first_dir_csv
}

dict_next_version = {
    "isSpaghettiCode": is_spaghetti_code_second_csv,
    "isGodClass": is_god_class_second_csv,
    "isFunctionalDecomposition": is_functional_decomposition_second_csv,
    "isClassDataShouldBePrivate": is_class_data_should_be_private_second_csv,
    "isComplexClass": is_complex_second_csv,
    "isMiddleMan": isMiddleMan_second_dir_csv,
    "isRefusedBequest": isRefusedBequest_second_dir_csv
}

list_files = ["isClassDataShouldBePrivate", "isComplexClass", "isMiddleMan",
              "isGodClass", "isFunctionalDecomposition",
              "isSpaghettiCode", "isRefusedBequest"
              ]

for name_file in list_files:
    current_file = dict_current_version.get(name_file)
    next_file = dict_next_version.get(name_file)
    print(next_file)
    list_csv = [current_file, next_file]
    dfs_concat = pd.concat(list_csv)
    dfs_list_class_name = pd.DataFrame(dfs_concat, columns=['Class Name'])
    duplicateDFRows = dfs_list_class_name[dfs_list_class_name.duplicated()]
    only_dup = dfs_concat[dfs_concat.duplicated(["Class Name"], keep=False)]
    path_to_save = "/home/broke31/Desktop/test/combined_proj/" + name_folder + "/" + get_parent(
        first_folder, 1) \
                   + "--" + get_parent(second_folder, 1)
    if not os.path.exists(path_to_save):
        os.makedirs(path_to_save)
    only_dup.to_csv(
        path_to_save + "/" + name_file + ".csv", index=False)
