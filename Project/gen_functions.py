# Python code to search .mp3 files in current
import os
import pickle

from Project.gen_util import parse

# Find your mp3 folder
dir_path = "C:/Users/Nabeel Arif/Desktop/MP3 Songs"
mp3_list = []


def gen_list():
    try:
        # Change the working directory
        os.chdir(dir_path)
        for root, dirs, files in os.walk(dir_path):
            for file in files:

                # change the extension from '.mp3' to
                # the one of your choice.
                if file.endswith('.mp3'):
                    mp3_list.append(str(file))
    except OSError:
        print("Can not find folder")

    dict_list = []
    for i in range(0, len(mp3_list)):
        sub_dict = parse(mp3_list[i])
        dict_list.append(sub_dict)

    if os.path.getsize('tracks.txt') is 0:
        upload(dict_list)


def upload(mp3_list):
    file = open('tracks.txt', 'wb')
    pickle.dump(mp3_list, file)
    file.close()


def retrieve():
    file = open('tracks.txt', 'rb')
    dict_list = pickle.load(file)
    return dict_list
