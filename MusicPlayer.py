# importing necessary modules

import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import os

mainColor = '#17202A'

window = tk.Tk()
window.title("Giosoco")
window.configure(bg=mainColor)
window.geometry("500x500")

mixer.init()

global dictionary
dictionary = {'E.S. Posthumus - Nara': 'D:\Music\Independent\E.S. Posthumus - Nara.mp3',
              'Against All Odds': "D:\Music\Moonlight Shadows\\05 Against All Odds.mp3"}


def play(*args):
    try:
        song = list.get('anchor')
        mixer.music.load(dictionary[song])
        mixer.music.play()
    except:
        pass

def pauseplay():
    if mixer.music.get_busy() == True:
        mixer.music.pause()
        PausePlay.configure(text='Play')
    else:
        pass

def browseSong():
    file = filedialog.askopenfilenames()
    browsePath = str(file)[2:len(str(file))-3]
    mixer.music.load(browsePath)
    mixer.music.play()
    songName = os.path.basename(browsePath)
    dictionary[songName] = browsePath
    y = list.size()
    list.insert(y, songName)

Play = tk.Button(text='Play from Beginning', command=play)
Play.grid(row=0, column=1)
PausePlay = tk.Button(text='Pause', command=pauseplay, width=10)
PausePlay.grid(row=0, column=2)

Box = tk.LabelFrame(window, text='ADD SONGS', font='Courier 12')
Box.grid(column=0, row=3)

emptyLabel = tk.Label(bg=mainColor)
emptyLabel.grid(column=0, row=2)

browseSongs = tk.Button(Box, text='Browse', width=16, command=browseSong)
browseSongs.grid(row=2, column=0)

list = tk.Listbox(window)
list.grid(row=1, column=0)
list.insert(0, 'E.S. Posthumus - Nara')
list.insert(1, 'Against All Odds')
list.bind('<<ListboxSelect>>', play)

window.mainloop()
