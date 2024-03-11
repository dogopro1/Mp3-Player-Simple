import os
import pygame
import tkinter as tk
from tkinter import filedialog

def play_music():
    selected_song = listbox.get(tk.ACTIVE)
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def load_music():
    folder = filedialog.askdirectory()
    os.chdir(folder)
    songs = [file for file in os.listdir(folder) if file.endswith(".mp3")]
    for song in songs:
        listbox.insert(tk.END, song)

# Application initialization
root = tk.Tk()
root.title("MP3 Player")

# Pygame initialization and mixer
pygame.init()
pygame.mixer.init()

# Track list
listbox = tk.Listbox(root, width=60)
listbox.pack(pady=20)

# button
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=7)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=5)

load_button = tk.Button(root, text="Load music folder", command=load_music)
load_button.pack(pady=11)

# Starting the main program loop
root.mainloop()
