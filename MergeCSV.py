import os
import glob
import pandas as pd

def merge_csv(path):
    os.chdir(path)
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    combined_csv = pd.concat([pd.read_csv(f, sep=";") for f in all_filenames])
    # export to csv
   # combined_csv.to_csv("combined.csv", index=False, encoding='utf-8-sig')
    return combined_csv

import os
import glob
import pandas as pd

def merge_csv(path):
    os.chdir(path)
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    combined_csv = pd.concat([pd.read_csv(f, sep=";") for f in all_filenames])
    # export to csv
   # combined_csv.to_csv("combined.csv", index=False, encoding='utf-8-sig')
    return combined_csv


base_dir = "/home/broke31/Desktop/Lav_riuso/RQ2_change_label_cop/"
path_to_save = "/home/broke31/Desktop/Lav_riuso/RIS_COMPLETE_RQ2/"
type_of_smell = "is_spaghetti"
extension = 'csv'
os.chdir(base_dir+type_of_smell)

all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])#export to csv
to_save_complete = path_to_save+type_of_smell+"/"
if not os.path.exists(to_save_complete):
    os.makedirs(to_save_complete)

combined_csv = combined_csv.sort_values(by=['Project'])
combined_csv.to_csv(to_save_complete+type_of_smell+".csv", index=False, encoding='utf-8-sig')

