# Reveals a secret message from a unordered bunch of photos
# You can download an example zip of photos, from https://s3.amazonaws.com/udacity-hosted-downloads/ud036/prank.zip
# You also can download the photos from the current repository

import os

def rename_files():
    # get file names from a folder
    file_list = os.listdir(r"C:\Python-secret-message\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working directory: " + saved_path)
    os.chdir(r"C:\Python-secret-message\prank")
    # for each file, rename filename
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
