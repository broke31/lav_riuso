import os
from glob import glob
from pathlib import Path


def get_list_file_csv(base):
    result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(base) for f in filenames if
              os.path.splitext(f)[1] == '.csv']
    return result


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


def remove_ext(name_file):
    return name_file.rsplit('.', 1)[0]


def get_sub_dir(path):
    return os.listdir(path)


def get_version_from_file(path, smell):
    print(smell)
    s = get_parent(path,1)
    s1 = s.split(smell)
    return s1[0]
