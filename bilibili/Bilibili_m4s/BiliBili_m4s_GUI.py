# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:13:55 2019

@author: david
"""

import os, re
from ffmpy import FFmpeg
import tkinter as tk
from tkinter import filedialog


window = tk.Tk()
window.title('B站缓存m4s合并')
window.geometry('500x200')
current_directory = filedialog.askdirectory()
output_name = current_directory.split("/")[2]
print(current_directory)

def video_audio_mux():
    if num_file == 1:
        output_filepath = current_directory + "/" + output_name + ".mp4"
    else:
        output_filepath = current_directory + "/" + output_name  + "_" + str(file_index + 1) + ".mp4"
    print(output_filepath)
    ff = FFmpeg(
        inputs={audio_list[file_index]:None,video_list[file_index]:None},
        outputs={output_filepath:'-codec copy'}
        ) 
    ff.run()    

def match_filename():
    global audio_list
    global video_list
    for root, dirs, files in os.walk(current_directory):
        for name in files:
            if re.match('audio.m4s', name):
                audio_list.append(os.path.join(root, name))
            if re.match('video.m4s', name):
                video_list.append(os.path.join(root, name))
                
                
def quit_window():
    global window
    window.destroy()

audio_list = []
video_list = []
match_filename()


num_file = len(audio_list)
flag = 0
for file_index in range(num_file):
    flag = flag + 1

    video_audio_mux()

    if flag == num_file:
        lable = tk.Label(window, text='转换完成', bg='green', font=('Arial', 20), width=30, height=2)
        button = tk.Button(window, text="退出", font=('Arial', 15), command = quit_window)
        lable.pack()
        button.pack()
        window.mainloop()
        

