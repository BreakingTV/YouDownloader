import pytube
import os


def main():
    yp = pytube.Playlist(input("URL: "))

    os.mkdir(yp.title)
    os.chdir(yp.title)

    for v in yp.video_urls:
        video = pytube.YouTube(v)

        stream = video.streams.filter(res="720p").first()
        print("Downloading: " + stream.title)
        stream.download()
        print("Downloaded " + stream.title)

    print("All Videos Downloaded!")
