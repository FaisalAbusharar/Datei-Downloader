# Penitus-Downloader


This code provides functions and classes for downloading files from the internet.

## Installation
To use this code, you will need to install the following libraries:

`pytube`: a library for downloading YouTube videos
`requests`: a library for making HTTP requests

You can install these libraries using pip:


`pip install pytube requests`
## Functions and Classes
## `download_youtube_video(url, folder, filetype)`
This function downloads a video from YouTube given a URL and saves it to a specified folder with a specified file type. It uses the PyTube library to accomplish this task.

Parameters:
* `url`: A string representing the URL of the YouTube video to be downloaded.
* `folder`: A string representing the path of the folder where the downloaded video will be saved.
* `filetype`: A string representing the file type of the video to be downloaded (e.g. 'mp4', 'webm').
## `Downloader(threading.Thread)
This class is a subclass of `threading.Thread` and it has an `__init__` method that takes three arguments: `url`, `filename`, and `folder`.

Parameters:
* `url`: A string representing the URL of the file to be downloaded.
* `filename`: A string representing the name of the file that will be used to save the downloaded file.
* `folder`: A string representing the path of the folder where the downloaded file will be saved.

The `run` method of this class attempts to download a file from the URL specified in the `url` argument and save it to the specified `folder` with the specified `filename`. If the URL is a Spotify track URL, the function extracts the track ID from the URL, requests an access token from the Spotify API using the `ID` and `SECRET` variables, and uses the access token to make a request for the track metadata and track audio data. It then saves the audio data to a file with the `filename` specified in the `__init__` method.


Make sure to have downloaded these libraries before attempting to use the file downloader.


## Spotify Support

To use spotify with this File Downloader, you need to go to create an app in the spotify [Developer DashBoard](https://developer.spotify.com/dashboard/applications), take the ID and the Secret and replace
the `ID` and `SECRET` with your own credentials.
