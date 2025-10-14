import os

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
            os.mkdir("C:\\Users\\School Account\\Downloads\\"+ "" + i)
    except:
        print("folder already exist")
create_path()