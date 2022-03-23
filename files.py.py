__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

#1 creates a folder if it doesn't already exists. if it exists, loops through its files and empties it

import os
import shutil

def clean_cache():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_directory, 'cache')
    isdir = os.path.isdir(path)
    if isdir:
        for file_name in os.listdir(path):
            file = os.path.join(path, file_name)
            if os.path.isfile(file):
                os.remove(file)
    else: 
        path_cache = os.path.join(current_directory, 'cache')
        os.mkdir(path_cache)
        
clean_cache()

#2 unzips file

def cache_zip(zip_file, dir_path):
    shutil.unpack_archive(zip_file, dir_path)

cache_zip("C:\\Users\\Monica Onutu\\Winc\\files\\data.zip", 'C:\\Users\\Monica Onutu\\Winc\\files\\cache' )    #double \\ needed to escape escaping... 

#3 returns list of files in absolute terms

def cached_files():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_directory, 'cache')
    absolute_paths = []
    for file_name in os.listdir(path):
        file = os.path.join(path, file_name)
        if os.path.isfile(file):
                absolute_paths.append(file)
    return absolute_paths
            
print(cached_files())


#4 reads files, returns line with condition

def find_password(absolute_paths):
    for path in absolute_paths:
        with open(path, 'r') as f: 
            contents = f.readlines()
            for line in contents:
                if 'password' in line:
                    password = line
                    password = password.replace(" ", "")
                    password = password.replace("password:", "")
                    return (password)
                
print(find_password(cached_files()))
