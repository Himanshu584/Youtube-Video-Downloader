# Youtube-Video-Downloader
These simple yet powerfull few lines of code will download n numbers of youtube videos in high resolution , i.e. 720p for you.

Python package used here is -- pytube ,  which is an youtube video package for python.


# Code Explanation
first we begin by importing the required library. Then we make an empty list in which all the urls for videos.
then we start a while loop so that person can enter desired numbers of URL's before ending the loop with "E".
then we append those URL's to the empty list we initialized before running the while loop.
further we initialize a for loop with x,video in enumerate(list), where x represents the index of item in the list and video represents the url corresponding to that index.
then we create a youtube instance for the video and get the stream by itag value of 22 which represents 720p resolution. finally we download the video with stream.download().
