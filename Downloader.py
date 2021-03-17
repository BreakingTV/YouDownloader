import os
import shutil
import pytube

import urllib.request
import re

search_keyword = input("Name/URL: ")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
result = "https://www.youtube.com/watch?v=" + video_ids[0]

youtube_video = pytube.YouTube(result)
stream = youtube_video.streams.get_highest_resolution()

stream.download()

print("Download Successful")

shutil.move(stream.title + ".mp4", input("Where you want to store this video? Full path: ") + "/")
