__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os, zipfile, shutil

def clean_cache():
    cache_path = os.path.join(os.getcwd(), "cache")
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
    os.mkdir(cache_path)

def cache_zip(zip_file_path, cache_dir_path):
    # Delete the existing cache directory
    clean_cache()

    # Extract the zip file to the cache directory
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(cache_dir_path)


def cached_files():
    cache_path = os.path.join(os.getcwd(), "cache")
    files = []
    # list all files and folders and iterate to check if it is a file
    for file in os.listdir(cache_path):
        if os.path.isfile(os.path.join(cache_path, file)):
            # add cache path and file name to files
            files.append(os.path.abspath(os.path.join(cache_path, file)))
    return files


def find_password(file_path_list):
    password = None
    for file_path in file_path_list:
        with open(file_path, "r") as f:
            for line in f:
                if "password" in line:
                    password = line.split(":")[1].strip()
                    break
        if password is not None:
            break
    return password