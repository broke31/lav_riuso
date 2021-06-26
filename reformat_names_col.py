import os

import pandas as pd

from FileSystem import get_sub_dir, get_list_file_csv

base_dir ="/home/broke31/Desktop/Lav_riuso/RQ2_with_proj/"
to_save = "/home/broke31/Desktop/Lav_riuso/RQ2_change_label/"

sub_dir = get_sub_dir(base_dir)

for folder in sub_dir:
    versions = get_sub_dir(base_dir+"/"+folder)
    for version in versions:
        list_of_smells = get_sub_dir(base_dir+"/"+folder+"/"+version)
        complete_list_csv  = get_list_file_csv(base_dir+folder+"/"+version+"/")
        for smell in list_of_smells:
            x= get_list_file_csv(base_dir + folder + "/" + version + "/"+smell)
            print(x)
            csv = pd.read_csv(x[0])
            print(csv)
            l = version.split("-")
            currrent_v = l[0]
            next_v = l[1]
            rep = []
            for name_col in csv.columns:
                name_col= name_col.replace(currrent_v,"current version")
                name_col= name_col.replace(next_v,"next version")
                rep.append(name_col)
            print(rep)
            csv.columns = rep
            print(csv)
            #path_to_save = to_save+folder+"/"+version+"/"+sme".csv"
            print(x)
            path_to_save = to_save+folder+"/"+smell+"/"

            if not os.path.exists(path_to_save):
                os.makedirs(path_to_save)
            csv.to_csv(path_to_save+currrent_v+"-"+next_v+".csv",index= False)
