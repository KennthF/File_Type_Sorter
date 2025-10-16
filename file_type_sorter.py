import os
from pathlib import Path

download_dir = str(os.path.join(Path.home(), "Downloads"))

def create_path():
    ''' creates paths for different type of file '''
    file_type = {
        "img" : "Pictures",
        "doc" : "Documents",
        "sound" : "Sounds",
        "vid" : "Videos"
    }

    #We can try reading the folder first if it exist or not
    try:
        for i in file_type.values():
            os.mkdir(download_dir + "\\" + i)
    except:
        print("folder already exist")

def files_sort():
    for files in os.listdir(download_dir):
        print(f"File Name: {files}")

create_path()



