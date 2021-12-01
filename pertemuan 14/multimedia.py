import pygame
import tkinter as tkr
import os

# membuat window
player = tkr.Tk()

# edit window
player.title("Audio Player | Kreshna Putra")
player.geometry("350x450")

# playlist
os.chdir("playlist")
print(os.chdir)
songlist = os.listdir()

# volume
VolumeLevel = tkr.Scale(player, from_=0.1, to_=1.0,
                        orient=tkr.HORIZONTAL, resolution=0.1)

# input playlist
# playlist = tkr.Listbox(player,  selectmode=tkr.SINGLE)
playlist = tkr.Listbox(player, highlightcolor="darkMagenta", selectmode=tkr.SINGLE)
print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

# pygame init
pygame.init()
pygame.mixer.init()

# aksi event


def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get())
    print(pygame.mixer.music.get_volume())
    print(VolumeLevel.get())

def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def UnPause():
    pygame.mixer.music.unpause()

# membuat button
Button1 = tkr.Button(player, width=5, height=2, text="PLAY", command=Play)
Button2 = tkr.Button(player, width=5, height=2,
                     text="STOP", command=ExitPlayer)
Button3 = tkr.Button(player, width=5, height=2, text="PAUSE", command=Pause)
Button4 = tkr.Button(player, width=5, height=2,
                     text="UNPAUSE", command=UnPause)

# judul lagu
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)

# place widget
songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
VolumeLevel.pack(fill="x")
playlist.pack(fill="both", expand="yes")

# aktif
player.mainloop()