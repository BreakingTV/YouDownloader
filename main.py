from Options import URL, playlist, video

Option = input("option:").lower()

if Option == "video".lower():
    video.main()
elif Option == "URL".lower():
    URL.main()
elif Option == "playlist".lower():
    playlist.main()
