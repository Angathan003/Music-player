import os
import pygame

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def create_playlist(directory):
    playlist = []
    for file in os.listdir(directory):
        if file.endswith(".mp3") or file.endswith(".wav"):
            playlist.append(os.path.join(directory, file))
    return playlist

pygame.init()
pygame.mixer.init()

audio_directory = input("Enter the audio directory path: ")

if not os.path.isdir(audio_directory):
    print("Invalid directory path.")
    exit()

playlist = create_playlist(audio_directory)

if not playlist:
    print("No audio files found in the specified directory.")
    exit()

play_music(playlist[0])

while True:
    command = input("Enter command (next, pause, resume, stop): ")
    if command == "next":
        pygame.mixer.music.stop()
        if playlist:
            playlist.pop(0)
            if playlist:
                play_music(playlist[0])
            else:
                print("Playlist finished.")
    elif command == "pause":
        pygame.mixer.music.pause()
    elif command == "resume":
        pygame.mixer.music.unpause()
    elif command == "stop":
        pygame.mixer.music.stop()
        break
    else:
        print("Invalid command.")

pygame.quit()
