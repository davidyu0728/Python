# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:45:16 2019

@author: david
"""
from tinytag import TinyTag
import os
import re
path = os.getcwd()
file_name = os.listdir()
name_dict = {}
try:
    os.remove('musiclist.txt')
except FileNotFoundError:
    pass


def error_encode(filename):
    try:
        filename.encode("gb2312")
    except UnicodeEncodeError:
        return True
'''     
def is_num_filename(filename):
    file_name = re.sub(r'_',"",filename) 
    file_name = re.compile(r'\d+')
'''
        
def find_musictag():
    for file in file_name:
        list_name = os.path.splitext(file)
        filename = list_name[0]
        
        if error_encode(filename):
            if list_name[1] == '.flac':
                tag = TinyTag.get(file)
                title = tag.title
                num = tag.track
                if len(str(num)) == 1:
                    name_dict[list_name[0]] = str(0)+str(num)+"_"+title
                else:
                    name_dict[list_name[0]] = str(num)+"_"+title
                print(name_dict)
                
        else:
            if list_name[1] == '.flac':
                tag = TinyTag.get(file)
                title = tag.title
                num = tag.track
                if len(str(num)) == 1:
                    name_dict[list_name[0]] = str(0)+str(num)+"_"+title
                else:
                    name_dict[list_name[0]] = str(num)+"_"+title
                print(name_dict)
    return name_dict


def rename_musicfile():
    find_musictag()
    for file in file_name:
        list_name = os.path.splitext(file)
        if list_name[1] == '.flac':
            changefilename = name_dict[list_name[0]] + '.flac'
            os.rename(file, changefilename)
    

rename_musicfile()
    
