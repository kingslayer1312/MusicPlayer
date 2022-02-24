# importing necessary modules
# added this comment 24.02.2022

import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import os
from time import strftime
from time import gmtime
from mutagen.mp3 import MP3

mainColor = '#17202A'

window = tk.Tk()
window.title("Giosoco")
window.configure(bg=mainColor)
window.geometry("500x500")

mixer.init()

global songList
songList = []

global pathList
pathList = []

global path
path = ''


def play(*args):
    global path
    try:
        song = list.get('anchor')
        x = songList.index(song)
        path = pathList[x]
        mixer.music.load(path)
        mixer.music.play()
        PausePlay.configure(image=pauseImage)
        songTime()
    except:
        pass


def pauseplay():
    if mixer.music.get_busy():
        mixer.music.pause()
        PausePlay.configure(image=playImage)
    else:
        mixer.music.unpause()
        PausePlay.configure(image=pauseImage)


def rewind():
    global path
    try:
        currsong = list.selection_get()
        index = songList.index(currsong) - 1
        print(currsong)
        list.selection_clear(0, 'end')
        list.selection_set(index)
        list.activate(index)
        path = pathList[index]
        mixer.music.load(path)
        mixer.music.play()
    except:
        pass


def slide(*args):
    pass


def forward():
    global path
    try:
        currsong = list.selection_get()
        index = songList.index(currsong) + 1
        print(currsong)
        list.selection_clear(0, 'end')
        list.selection_set(index)
        list.activate(index)
        path = pathList[index]
        mixer.music.load(path)
        mixer.music.play()
    except:
        pass


def browseSong():
    global songList
    global pathList
    global path
    try:
        if os.name == 'nt':
            file = filedialog.askopenfilenames(initialdir='\Music')
        elif os.name == 'posix':
            file = filedialog.askopenfilenames(initialdir='/home/hrishikesh/Music')
        path = str(file)[2:len(str(file)) - 3]
        mixer.music.load(path)
        mixer.music.play()
        songName = os.path.basename(path)
        pathList.append(path)
        songList.append(songName)
        y = list.size()
        list.insert(y, songName)
        list.select_anchor(y)
        list.activate(y)
        list.selection_clear(0, tk.END)
        list.selection_set(y)
        PausePlay.configure(image=pauseImage)
        songTime()
    except:
        pass


def songTime():
    timeElapsed = (mixer.music.get_pos()) / 1000
    time = strftime("%H:%M:%S", gmtime(timeElapsed))
    timeLabel.config(text=time)
    timeLabel.after(1000, songTime)
    song = MP3(path)
    songLength = song.info.length
    slider.config(to=songLength)
    slider.set(timeElapsed)


pauseImage = tk.PhotoImage(file="pause.png")
playImage = tk.PhotoImage(file="play.png")
rewindImage = tk.PhotoImage(file="rewind.png")
forwardImage = tk.PhotoImage(file="forward.png")

PausePlay = tk.Button(command=pauseplay, bg='#F39C12', activebackground='#EE9201')
PausePlay.grid(row=1, column=3)

if mixer.music.get_busy():
    PausePlay.configure(image=pauseImage)
else:
    PausePlay.configure(image=playImage)

Rewind = tk.Button(command=rewind, bg='#F39C12', image=rewindImage, activebackground='#EE9201')
Rewind.grid(row=1, column=2)
Forward = tk.Button(command=forward, bg='#F39C12', image=forwardImage, activebackground='#EE9201')
Forward.grid(row=1, column=4)

slider = tk.Scale(window, from_=0, to=200, length=260, orient='horizontal', bg=mainColor, fg='white', showvalue=0)
slider.grid(row=2, columnspan=3, column=2, pady=20)

Box = tk.LabelFrame(window, text='Your Music', font='Courier 12')
Box.grid(column=0, row=0)
sliderFrame = tk.LabelFrame(window)
sliderFrame.grid(column=2, row=3, columnspan=3)

emptyLabel = tk.Label(bg=mainColor)
emptyLabel.grid(column=0, row=2)
emptyLabel2 = tk.Label(bg=mainColor, width=2)
emptyLabel2.grid(column=1, row=0)
timeLabel = tk.Label(sliderFrame, text='')
timeLabel.grid(column=0, row=0)

browseSongs = tk.Button(Box, text='Browse', width=16, command=browseSong)
browseSongs.grid(row=2, column=0)

list = tk.Listbox(Box, selectmode='browse')
list.grid(row=1, column=0)
list.bind('<<ListboxSelect>>', play)

window.mainloop()
