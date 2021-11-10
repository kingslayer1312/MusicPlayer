# importing necessary modules

from pygame import mixer
import tkinter as tk

window = tk.Tk()
window.title("BasicCalc")
window.configure(bg='#581845')
window.geometry("500x500")

mixer.init()

global dictionary
dictionary = {'Ab Tere Bin': 'D:\Music\Aashiqui\Ab Tere Bin.mp3',
              'Ek Sanam Chahiye': 'D:\Music\Aashiqui\Ek Sanam Chahiye.mp3'}


def play(*args):
    song = list.get('anchor')
    mixer.music.load(dictionary[song])
    mixer.music.play()


def pauseplay():
    if mixer.music.get_busy() == True:
        mixer.music.pause()
        PausePlay.configure(text='Play')
    else:
        mixer.music.unpause()
        PausePlay.configure(text='Pause')




def addSongs():
    addSongEntry.configure(state='normal')
    addSongPath.configure(state='normal')


def ok():
    x = list.size()
    list.insert(x, addSongEntry.get())
    path = addSongPath.get()
    path = path.replace('"', '')
    dictionary[addSongEntry.get()] = path


Play = tk.Button(text='Play from Beginning', command=play)
Play.grid(row=0, column=1)
PausePlay = tk.Button(text='Pause', command=pauseplay)
PausePlay.grid(row=0, column=2)
addSongs = tk.Button(text='Add Songs', command=addSongs)
addSongs.grid(row=1, column=2)
ok = tk.Button(text='OK', command=ok)
ok.grid(row=4, column=2)

addSongEntry = tk.Entry()
addSongEntry.grid(row=2, column=2)
addSongEntry.configure(state='disabled')
addSongEntry.insert(0, "Enter song name")

addSongPath = tk.Entry()
addSongPath.grid(row=3, column=1)
addSongPath.configure(state='disabled')
addSongPath.insert(0, "Enter song path")

list = tk.Listbox(window)
list.grid(row=1, column=0)
list.insert(0, 'Ab Tere Bin')
list.insert(1, 'Ek Sanam Chahiye')
list.bind('<<ListboxSelect>>', play)

window.mainloop()
