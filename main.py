import os
import time

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

path = input("Enter the path of a folder containing music: ")


def songlist(path):
    try:
        files = (os.listdir(path))
    except:
        print("Unable to open the directory!")
        return []
    songs = []
    for i in files:
        if i.endswith(".mp3") or i.endswith(".wav"): songs.append(i)
    print("\nSongs' list contains following tracks:")
    # for title in songs: print(title)
    for i in range(len(songs)): print("%.2d. %s" % (i + 1, songs[i]))
    if len(songs) == 0: print("\nNo playable media files are available at this location!")
    return songs


def songselect(songlist):
    x, num = 1, 0
    if len(songlist) != 0:
        while x:
            try:
                num = int(input("\nWhich song is to be played? (Enter a number): "))
                if num <= len(songlist):
                    x = 0
                else:
                    print("Max song number can be %d" % len(songlist))
            except:
                print("Enter a valid number!")
    return num - 1


def player(path="", songs=[], num=0):
    try:
        for i in range(num, len(songs)):
            loc = path + "\\" + songs[i]
            hrs, mnu, sec, t = 0, 0, 0, 0
            mixer.init()
            mixer.music.load(loc)
            mixer.music.play()
            print("\nNow playing \'%s\'..." % songs[i])
            while mixer.music.get_busy():  # wait for music to finish playing
                b = time.time()
                print("\r%02d:%02d:%02d" % (hrs, mnu, sec), end="")
                time.sleep(1 - t)
                sec += 1
                if (sec == 60):
                    mnu += 1
                    sec = 0
                    if (mnu == 60):
                        hrs += 1
                        mnu = 0
                        if (hrs == 24):
                            hrs = 0
                e = time.time()
                t = (e - b) - 1
        print("\n\nAll songs of the list are played\nTerminating the program in 5 sec", end='')
        mixer.quit()
        for i in range(5):
            print(".", end='')
            time.sleep(1)
    except:
        print("\n\nAn error occured!")


new = songlist(path)
num = songselect(new)
player(path, new, num)
