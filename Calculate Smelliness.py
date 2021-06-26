import os
from os.path import join

import pandas as pd

from FileSystem import get_sub_dir, get_list_file_csv
from Reformat import reformat_ant


def min_max(x):
    return (x - min(x)) / (max(x) - min(x))

def get_version(file,smell):
    to_return = file.split("/")
    print(to_return)


name_folder = "ant"

path_to_ris_rq2 = "/home/broke31/Desktop/Lav_riuso/ris_RQ2/" + name_folder
list_dirs = ["is_complex_data","is_functional_dec", "is_god_class",
             "is_spaghetti", "should_be_private"]

for dir in list_dirs:
        path_with_sub_dir = path_to_ris_rq2+"/"+dir
        print(path_with_sub_dir+"/")
        list_of_csv = get_list_file_csv(path_with_sub_dir+"/")
        print(list_of_csv)
        for file in list_of_csv:
            get_version(file, "is_complex_data")
            file_csv= pd.read_csv(path_with_sub_dir+file+".csv")
            exit(0)
            if dir == "is_complex_data":
                get_version(file,"is_complex_data")
                exit(0)
              #  file_csv["mcCabeMetric"] =


