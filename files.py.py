__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

#1 creates a folder if it doesn't already exists. if it exists, loops through its files and empties it

import os
import os.path

def clean_cache():
    directory = 'cache'
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = f'{current_directory}\cache\\'   # two \\ needed, just one returns error
    isdir = os.path.isdir(path)
    if isdir:
        for file_name in os.listdir(path):
            file = path + file_name
            if os.path.isfile(file):
                os.remove(file)
    else: 
        path_cache = os.path.join(current_directory,directory)
        os.mkdir(path_cache)
        
clean_cache()

#2 unzips file

import shutil

def cache_zip(zip_file, dir_path):
    shutil.unpack_archive(zip_file, dir_path)

cache_zip("C:\\Users\\Monica Onutu\\Winc\\files\\data.zip", 'C:\\Users\\Monica Onutu\\Winc\\files\\cache' )    #double \\ needed to escape escaping... 

#3 returns list of files in absolute terms

def cached_files():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = f'{current_directory}\cache\\'
    print(path)
    absolute_paths = []
    for file_name in os.listdir(path):
            file = path + file_name
            if os.path.isfile(file):
                absolute_paths.append(file)
    return absolute_paths
            
print(cached_files())


#4 reads files, returns line with condition

def find_password(absolute_paths):
    for path in absolute_paths:
        f = open(path, 'r')
        contents = f.readlines()
        for line in contents:
            if 'password' in line:
                return (line)
                
print(find_password(cached_files()))
