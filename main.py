import os
import re
import shutil
import sys
import urllib

import pytube

Option = input("option:").lower()

if Option == "video".lower():

    videos = [0, 1, 2, 3, 4, 5]

    async def name():
        search_keyword = input("Name: ").replace(" ", "+").lower()
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

        print("Loading...")
        print(" ")
        for v in videos:
            print("[" + str(v) + "]" + pytube.YouTube(
                "https://www.youtube.com/watch?v=" + video_ids[v]).title + " - " + pytube.YouTube(
                "https://www.youtube.com/watch?v=" + video_ids[v]).author)
        print(" ")
        print("Choose one video you want to download")

        inp = input()
        inp = int(inp)
        result = "https://www.youtube.com/watch?v=" + video_ids[inp]

        youtube_video = pytube.YouTube(result)
        print("Using: " + pytube.YouTube(result).title)

        stream = youtube_video.streams.filter(res="720p").first()

        print("when you don't know press Enter")
        inp = input("Where you want to store this video? Full path: ")

        if inp.startswith(""):
            print("Using file location")
        else:
            os.chdir(inp)
        print("Location is: " + inp + "/")

        stream.download()

        # stream_audio = youtube_video.streams.get_audio_only()
        # stream_audio.download("", "audio")

        # audio = mpe.AudioFileClip("audio.mp4")
        # video1 = mpe.VideoFileClip(stream.default_filename)
        # final = video1.set_audio(audio)
        # final.write_videofile("/home/danil/Videos/output.mp4", codec='mp4', audio_codec='libvorbis')

        print("Download Successful")

elif Option == "URL".lower():
    async def URL():
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

elif Option == "playlist".lower():
    async def playlist():
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

