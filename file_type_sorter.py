import os, shutil
from pathlib import Path

download_dir = str(os.path.join(Path.home(), "Downloads"))

file_type = {
    "jpg" : "Pictures", "jpeg" : "Pictures", "png" : "Pictures", "gif" : "Pictures", "bmp" : "Pictures", "tiff" : "Pictures", "tif" : "Pictures", "webp" : "Pictures", "heic" : "Pictures", "svg" : "Pictures", "ico" : "Pictures",
    "pdf" : "Documents", "doc" : "Documents", "docx" : "Documents", "txt" : "Documents", "rtf" : "Documents", "odt" : "Documents", "xls" : "Documents", "xlsx" : "Documents", "ppt" : "Documents", "pptx" : "Documents", "csv" : "Documents", "md" : "Documents", "log" : "Documents", "tex" : "Documents", "epub" : "Documents",
    "mp3" : "Sounds", "wav" : "Sounds", "aac" : "Sounds", "flac" : "Sounds", "ogg" : "Sounds", "m4a" : "Sounds", "wma" : "Sounds", "aiff" : "Sounds", "amr" : "Sounds",
    "mp4" : "Videos", "mov" : "Videos", "wmv" : "Videos", "avi" : "Videos", "mkv" : "Videos", "flv" : "Videos", "webm" : "Videos", "mpeg" : "Videos", "mpg" : "Videos", "3gp" : "Videos", "m4v" : "Videos"
}

folder_name = ["Pictures", "Documents", "Sounds", "Videos", "Other"]

def folder_creation():
    ''' creates paths for different type of file '''
    try:
        for folder in folder_name:
            os.mkdir(download_dir + "\\" + folder)
    except:
        print("folder already exist")

def file_sort():
    """ Sort Files to the specified dir """

    #Create the folder
    folder_creation()
    
    for file in os.listdir(download_dir): #list all the items in dir
        if os.path.isfile(download_dir + "\\" + file): #just get the file not folder
            ext = file.split(".") 
            folder_dest = file_type.get(ext[len(ext)-1]) #get the filetype

            if folder_dest:
                shutil.move(download_dir + "\\" + file, download_dir + "\\" + folder_dest + "\\" + file)
            else:
                shutil.move(download_dir + "\\" + file, download_dir + "\\" + "Other" + "\\" + file)

file_sort()

    


