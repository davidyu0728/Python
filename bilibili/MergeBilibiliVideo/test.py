# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 13:54:44 2018

@author: Bochao Yu
"""

import os
path = os.getcwd()

file_name = os.listdir()
filename_list = []


try:
    os.remove('videolist.txt')
except FileNotFoundError:
    pass

def change_suffix():
    for file in file_name:
        old_name = os.path.splitext(file)
        if old_name[1] == '.blv':
            new_name = old_name[0] + '.flv'
            os.rename(file, new_name)

def make_txtfile():
    txt_file = open('videolist.txt', 'w')
    for file in file_name:
        list_name = os.path.splitext(file)
        if list_name[1] == '.flv':
            #print(list_name[0])
            filename_list.append(list_name[0])
    b = sorted(filename_list, key=len)
    for i in range(len(b)):
        name = b[i] + '.flv'
        write_context = 'file ' + '\'' + name + '\'' + '\n'
        txt_file.write(write_context)
    txt_file.close()
    

if __name__ == '__main__': 
    print('changing suffix...')
    change_suffix()
    print('Done')
    print('making txtfile...')
    make_txtfile()
    print('Done')
    print('merge...')
    os.system('merge.bat')
