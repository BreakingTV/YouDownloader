import shutil
import pytube
import sys
import urllib.request
import re

videos = [0, 1, 2, 3]

search_keyword = input("Name/URL: ").replace(" ", "+").lower()

if search_keyword.startswith("https://"):
    print("Their can be some errors with the get https://")
    youtube_video = pytube.YouTube(search_keyword)
    stream = youtube_video.streams.filter(res="1080p").first()
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

else:
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
print("Loading...")

stream = youtube_video.streams.filter(res="1080p").first()

stream.download()

print("Download Successful")
print("when you don't know press Enter")
inp = input("Where you want to store this video? Full path: ")
if inp.startswith(""):
    sys.exit()
else:
    shutil.move(stream.default_filename, inp + "/")
