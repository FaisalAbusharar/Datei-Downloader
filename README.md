# Penitus-Downloader



This is a tool for downloading files, YouTube videos and (optionally) Spotify tracks.

## Prerequisites
* Python 3
* The following Python libraries: threading, requests, pytube, colorama

## Setup
- Clone this repository and navigate to the directory:
```
git clone https://github.com/<your-username>/youtube-and-spotify-downloader.git
cd youtube-and-spotify-downloader
```
- Install the required libraries:

```pip install -r requirements.txt```

- (Optional) Enable Spotify support:
When you first run the script, you will be prompted to enable Spotify support. If you choose to enable it, you will need to enter your Spotify client ID and client secret. These values can be obtained by creating a Spotify developer account and creating an app at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

## Usage
To download a YouTube video, run the script and enter the URL of the video when prompted. You can also specify a destination folder and filetype (e.g. `mp4` or `mp3`).

To download a Spotify track, you must first enable Spotify support as described above. Then, run the script and enter the URL of the track when prompted. Please note that due to limitations in the Spotify API, most tracks cannot be downloaded in full.

Here is an example of downloading a YouTube video:

```
python downloader.py
Enter the URL of what you want to download: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Limitations
- Due to limitations in the Spotify API, most Spotify tracks cannot be downloaded in full.
- The script is not capable of downloading private YouTube videos or tracks that are not available in your region.

## Disclaimer
This script is intended for educational purposes only. Please respect the terms of service of YouTube and Spotify, and do not use it to download copyrighted content without permission.