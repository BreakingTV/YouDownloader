import pytube
import sys
import shutil


def main():
    search_keyword = input("URL: ").replace(" ", "+").lower()
    print("Their can be some errors with the get https://")
    youtube_video = pytube.YouTube(search_keyword)
    stream = youtube_video.streams.filter(res="720p").first()
    print("Using: " + stream.title)
    print("Loading...")

    stream.download()
    print("Download Successful")
    print("when you don't know press Enter")
    inp = input("Where you want to store this video? Full path: ")
    if inp.startswith(""):
        sys.exit()
    else:
        shutil.move(stream.default_filename, inp + "/")
