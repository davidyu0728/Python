# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 00:34:15 2020

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
av_num = "av" + output_name
under_file = os.listdir(current_directory)
print(av_num)

def quit_window():
    global window
    window.destroy()
    
audio_list = []
video_list = []
for root, dirs, files in os.walk(current_directory):
    for name in files:
        
        if re.match('audio.m4s', name):
            audio_list.append(os.path.join(root, name))
        if re.match('video.m4s', name):
            video_list.append(os.path.join(root, name))


lable = tk.Label(window, text='转换完成', bg='green', font=('Arial', 20), width=30, height=2)
button = tk.Button(window, text="退出", font=('Arial', 15), command = quit_window)
lable.pack()
button.pack()
window.mainloop()
