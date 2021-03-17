import shutil
import pytube

import urllib.request
import re

search_keyword = input("Name/URL: ").replace(" ", "+").lower()

if search_keyword.startswith("https://"):
    youtube_video = pytube.YouTube(search_keyword)
    stream = youtube_video.streams.get_highest_resolution()

    stream.download()

    print("Download Successful")

    shutil.move(stream.title + ".mp4", input("Where you want to store this video? Full path: ") + "/")
else:
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    print("Loading...")
    print(" ")
    print("[1]" + pytube.YouTube("https://www.youtube.com/watch?v=" + video_ids[0]).title + " - " + pytube.YouTube("https://www.youtube.com/watch?v=" + video_ids[0]).author)
    print("[2]" + pytube.YouTube("https://www.youtube.com/watch?v=" + video_ids[1]).title + " - " + pytube.YouTube("https://www.youtube.com/watch?v=" + video_ids[1]).author)
    print("[3]" + pytube.YouTube("https://www.youtube.com/watch?v=" + video_ids[2]).title + " - " + pytube.YouTube("https://www.youtube.com/watch?v=" + video_ids[2]).author)
    print("[4]" + pytube.YouTube("https://www.youtube.com/watch?v=" + video_ids[3]).title + " - " + pytube.YouTube("https://www.youtube.com/watch?v=" + video_ids[3]).author)
    print("[5]" + pytube.YouTube("https://www.youtube.com/watch?v=" + video_ids[4]).title + " - " + pytube.YouTube("https://www.youtube.com/watch?v=" + video_ids[4]).author)
    print(" ")
    print("Choose one video you want to download")

inp = input()

if inp == "1":
    result = "https://www.youtube.com/watch?v=" + video_ids[0]

if inp == "2":
    result = "https://www.youtube.com/watch?v=" + video_ids[1]

if inp == "3":
    result = "https://www.youtube.com/watch?v=" + video_ids[2]

if inp == "4":
    result = "https://www.youtube.com/watch?v=" + video_ids[3]

if inp == "5":
    result = "https://www.youtube.com/watch?v=" + video_ids[4]

youtube_video = pytube.YouTube(result)
stream = youtube_video.streams.get_highest_resolution()
stream.download()
print("Download Successful")
shutil.move(stream.default_filename, input("Where you want to store this video? Full path: ") + "/")

