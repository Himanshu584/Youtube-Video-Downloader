import pytube  #--> python package for youtube video downloading

# make an empty list which will consist of all the urls of youtube videos
video_list = []
print("Enter video URL's , Terminate using 'E' ")

# Enter URL's to the list and run if key-E is entered
while True:
    urls = input("")
    if urls == "E":
        break
    video_list.append(urls)


for x, video in enumerate(video_list):    #--> x = index of video,  video = video URL at index x 
    v = pytube.YouTube(video)   
    stream = v.streams.get_by_itag(22)  #--> itag=22 reffers to 720px video quality
    print(f" Downloading video {x}...")
    stream.download()
    print("Video downloaded successfully!")

