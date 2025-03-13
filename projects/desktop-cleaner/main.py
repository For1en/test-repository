#!/bin/python3

import os

def create_folder(folder_name, dir_path):
    if folder_name.upper() not in os.listdir(dir_path):
        os.mkdir(folder_name.upper())
    else:
        print('amogus')

def clean_folder(dir_path):
    
    for file_name in os.listdir(dir_path):
        if os.path.isfile(f'{dir_path}/{file_name}'):
            file_type = file_name.split('.')[-1]
            create_folder(file_type, dir_path)
            file_path = os.path.join(dir_path, file_type.upper())
            print(file_path)
            os.system(f'mv "{file_name}" {file_path}')


clean_folder('/home/anton/Downloads/random')

