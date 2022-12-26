from pytube import YouTube
from pytube import Playlist
import string
import os.path
from os import path
from datetime import date
import random

def format_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
    return filename


# Creates a unique folder to download the file/playlist into, then moves the current working directory to the folder
def create_download_path(ytObject, downlaodPath=None):
    # Create a unique folder for the playlist download
    folder = format_filename(str(date.today()) + "-" + str(ytObject.title))

    if not path.exists(downlaodPath):
        raise ValueError("Invalid path, it does not exist")
    else:
        os.chdir(downlaodPath)
        if not path.exists(folder):
            os.mkdir(folder)
            os.chdir(folder)
            return os.getcwd()
        else:
            duplicateFolder = folder + str(random.randint(1, 100))
            os.mkdir(duplicateFolder)
            os.chdir(duplicateFolder)
            return os.getcwd()


# function for downloading a single video link
def download(link, createPath, downloadType=None, downloadPath=None):

    downloadTypes = ["video", "audio"]
    if downloadType not in downloadTypes:
        raise ValueError("Invalid download type. Expected one of %s" % downloadTypes)

    video = YouTube(link)

    if createPath == True:
        create_download_path(video, downloadPath)

    filename = format_filename(video.title + ".mp4")

    print("Starting download" + " - " + video.title + " - " + "at " + link)
    try:
        if downloadType == "video":
            video.streams.get_highest_resolution().download(filename=filename)
        elif downloadType == "audio":
            video.streams.filter(only_audio=True).first().download(filename=filename)
    except:
        print("An error has occurred with download", link)



# Function for downloading an entire playlist
def download_playlist(link, downloadType= "video", downloadPath=None):
    # Checks if the download type is valid
    downloadTypes = ["video", "audio"]
    if downloadType not in downloadTypes:
        raise ValueError("Invalid download type. Expected one of %s" % downloadTypes)

    loopNum = 0
    videoNum = 1

    playlist = Playlist(link)
    numVideos = playlist.length

    create_download_path(playlist, downlaodPath=downloadPath)

    print("There are", numVideos, "videos in this playlist")

    for video in playlist.videos:
        filename = format_filename(str(videoNum) + "_" + video.title + ".mp4")  # ensures the filename is valid

        print("Starting download " + str(videoNum) + "/" + str(numVideos) + ": " + video.title)
        try:
            if downloadType == "video":
                video.streams.get_highest_resolution().download(filename=filename)
            elif downloadType == "audio":
                video.streams.filter(only_audio=True).first().download(filename=filename)
        except:
            print("An error occurred with download", videoNum, video.title)

        loopNum += 1
        videoNum += 1
