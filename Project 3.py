import os, shutil

path = '/Users/prasad/Desktop/SQL/Automatic File Sorter'
files = os.listdir(path)
print(files)

folder_name = ['CSVFiles', 'Text Files', 'Image Files']

for folder in folder_name:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)


os.listdir(path)

file_name = os.listdir(path)
for file in file_name:
    if ".csv" in file and not o.path.exists(path + '/CSVFiles/' + file):
        shutil.move(path + file, path + '/CSVFiles/' + file)
    elif ".txt" in file and not os.path.exists(path + '/Text Files/' + file):
        shutil.move(path + file, path + '/Text Files/' + file)
    elif".png" in file and not os.path.exists(path + '/Image Files/' + file):
        shutil.move(path + file, path + '/Image Files/' + file)


path = '/Users/prasad/Desktop/SQL/Automatic File Sorter'


folder_name = ['CSVFiles', 'Text Files', 'Image Files']

for folder in folder_name:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)

file_name = os.listdir(path)


for file in fle_name:
    if ".csv" in file and not o.path.exists(path + '/CSVFiles/' + file):
        shutil.move(path + file, path + '/CSVFiles/' + file)
    elif ".txt" in file and not os.path.exists(path + '/Text Files/' + file):
        shutil.move(path + file, path + '/Text Files/' + file)
    elif".png" in file and not os.path.exists(path + '/Image Files/' + file):
        shutil.move(path + file, path + '/Image Files/' + file)