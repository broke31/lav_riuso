import pandas as pd

path_dir1 = "/home/broke31/Desktop/test/junit_new/"
path_dir2 = "/home/broke31/Desktop/Lav_riuso/RQ2/junit/"
name_folder ="junit4.2-junit4.6"
current = "junit-4.2"
next = "junit-4.6"

csv_dir1_current = pd.read_csv(path_dir1+name_folder+"/"+current+".csv")
print(csv_dir1_current)
csv_dir1_current['Class Name'] = csv_dir1_current["Class Name"].str.replace('.java' , '')
csv_dir1_next = pd.read_csv(path_dir1+name_folder+"/"+next+".csv")
csv_dir1_next['Class Name'] = csv_dir1_next["Class Name"].str.replace('.java' , '')

csv_dir2_current = pd.read_csv(path_dir2+name_folder+"/"+current+".csv")
csv_dir2_next = pd.read_csv(path_dir2+name_folder+"/"+next+".csv")

print(csv_dir1_current)
print(csv_dir2_current)

df_current = csv_dir1_current.merge(csv_dir2_current, left_on='Class Name', right_on='Nome del tipo')
print(df_current)