# Penitus-Downloader

Penitus Downloader is a script that allows you to download files from the internet. It starts by asking the user to input URLs to download, and then it creates a new thread for each URL. If the URL is a YouTube video, the code uses the pytube library to download the video. Otherwise, it uses the requests library to download the file and save it to the specified folder.

The script also includes some basic error handling to check if the URL is valid and to handle situations where the URL is not a YouTube video or a file that can be downloaded using the requests library.

The script uses the threading library to create and run threads, which allows you to perform multiple downloads concurrently. This can be useful for downloading multiple files at the same time and speeding up the overall process.

## Libraries

* pytube
* requests
* threading
* time
* os

Make sure to have downloaded these libraries before attempting to use the file downloader.
