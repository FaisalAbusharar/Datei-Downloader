import threading
import requests
import os
import time
import pytube
import base64
import json
from colorama import Fore, Style



global spotify_credentials


def get_spotify_credentials():


    id = input("Enter your Spotify client ID: ")
    secret = input("Enter your Spotify client secret: ")

    # Store the client ID and client secret in a dictionary
    spotify_credentials = {
        "Client_Token": id,
        "Client_Secret": secret,
        "Spotify_Enabled": True
    }

    

    # Write the dictionary to a JSON file called hidden.json
    with open('./hidden.json', 'w') as f:
        json.dump(spotify_credentials, f)

    Enabled = True

    input(Fore.LIGHTMAGENTA_EX + "A restart is required to apply the changes, press Enter")
    print(Style.RESET_ALL)
    quit()



try:
    os.system("cls")
    with open('hidden.json', 'r') as f:
            data = json.load(f)

    id = data["Client_Token"]
    secret = data["Client_Secret"]
    Enabled = data["Spotify_Enabled"]
except:
    

    os.system("cls")
    if not os.path.exists('hidden.json'):
        
        while True:
            choice = input(Fore.BLUE + "Do you want to enable Spotify support? (y/n) " + Fore.WHITE)
            if choice.lower() == 'y':
                
                get_spotify_credentials()
                break
            
            elif choice.lower() == "n":
                spotify_credentials = {
                "Spotify_Enabled": False
            }
           
                with open('hidden.json', 'w') as f:
                    json.dump(spotify_credentials, f)
                
                break
            else:
                print(Fore.BLUE + "Please input y/n\n\n")
            
            

    else:
        with open('./hidden.json', 'r') as f:
            data = json.load(f)
        try:
            id = data["Client_Token"]
            secret = data["Client_Secret"]
        except:
            pass
        Enabled = data["Spotify_Enabled"]
try:
    if Enabled == True:        
        input(Fore.RED + "Keep in mind while downloading using spotify, you cannot download " + 
                "the full song due to spotify's api. Most songs also cannot be downloaded.")
        Enabled = True
except:
    pass
       



def download_youtube_video(url, folder, filetype):
    


    start_time = time.time()  # record the start time
    yt = pytube.YouTube(url)
    print(Fore.LIGHTMAGENTA_EX + f"{yt.title}"+ Fore.CYAN + " is downloading...\n")
    print("-----------------------------------------------------------------------------")
    # Filter the available streams by filetype
    streams = yt.streams.filter(file_extension=filetype)
    # Select the first stream that matches the filetype
    video = streams.first()
    video.download(folder)
    end_time = time.time()  # record the end time
    elapsed_time = end_time - start_time  # calculate the elapsed time
    print(Fore.LIGHTMAGENTA_EX + f"{yt.title}" + Fore.LIGHTGREEN_EX +
     f" has been downloaded to {folder} with the filetype {filetype} in " +
      Fore.LIGHTRED_EX +  f"{elapsed_time:.2f} seconds.\n")



class Downloader(threading.Thread):
    def __init__(self,url,filename,folder):
        threading.Thread.__init__(self)
        self.url =url
        self.filename = filename
        self.folder = folder

    def run(self):
            
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
                    
            global start_time

            start_time = time.time()
            if "spotify" in self.url and Enabled == True:
            # Extract the track ID from the URL
                    track_id = self.url.split("track/")[1]
                    
                    # Set up the authorization header for the Spotify API
                    client_id = id
                    client_secret = secret
                    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode())
                    headers = {
                        "Authorization": f"Basic {auth_header.decode()}"
                    }
                    
                    # Request an access token from the Spotify API
                    token_response = requests.post("https://accounts.spotify.com/api/token", data={
                        "grant_type": "client_credentials"
                    }, headers=headers)
                    access_token = token_response.json()["access_token"]
                    
                    # Use the access token to make a request for the track metadata
                    track_response = requests.get(f"https://api.spotify.com/v1/tracks/{track_id}", headers={
                        "Authorization": f"Bearer {access_token}"
                    })
                    track_metadata = track_response.json()
                    
                    # Extract the track name from the metadata
                    track_name = track_metadata["name"]
                    
                    # Extract the artist name from the metadata
                    artist_name = track_metadata["artists"][0]["name"]
                    
                    # Construct the filename for the downloaded track
                    filename = f"{artist_name} - {track_name}.mp3"
                    file_path = os.path.join(self.folder, filename)

                    print(Fore.YELLOW + f"Downloading {track_name}.....")
                    
                    # Use the access token to make a request for the track audio data
                    try:
                        audio_response = requests.get(track_metadata["preview_url"], headers={
                            "Authorization": f"Bearer {access_token}"
                        })
                    except requests.exceptions.MissingSchema:
                        print("This song could not be downloaded, due to copyright reasons most likely")
                        return
                        
                    
                    # Save the audio data to the file
                    with open(file_path, "wb") as f:
                        f.write(audio_response.content)
                    
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    
                    print(Fore.LIGHTMAGENTA_EX + f"{filename}" + Fore.LIGHTGREEN_EX +
                    " has been downloaded to " + Fore.YELLOW +
                     f"{self.folder}" + Fore.LIGHTGREEN_EX + f" in {elapsed_time:.2f}")
                    return

        
            if "youtube" in self.url:
                filetype = "mp4"
                
                download_youtube_video(self.url, self.folder, filetype)
                return

            try:
                response = requests.get(self.url, stream=True) #Here we get request the data using requests.get, and inputing the url
                print(Fore.LIGHTMAGENTA_EX + f"{self.filename}"  + Fore.CYAN +  " is downloading...\n")
                print("-----------------------------------------------------------------------------")
            except:
                print(Fore.RED + f"The url inputed for {self.filename} is not a vaild type of url to download\n This file will not be downloaded and skipped.\n")
                return

            try:
                file_path = os.path.join(self.folder,self.filename)
                with open(file_path,"wb") as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
            except:
                print(Fore.RED + "An error has occured, this could be because of the URL you are using")

            end_time = time.time()  # record the end time
            elapsed_time = end_time - start_time  # calculate the elapsed time
            
            print(Fore.LIGHTMAGENTA_EX + f"{self.filename} Thread has finished in "  + Fore.LIGHTRED_EX + f"{elapsed_time:.2f} seconds.\n")



urls=[]
while True:
    url = input(Fore.BLUE + "Type a URL to download (N to Finish) " + Fore.WHITE)
    if url.lower() == "n":
        if len(urls) == 0:
            print(Fore.BLUE + "You have not inputed any url, input one please, or press Q to quit\n" + Fore.WHITE)
        else:
            break
    elif url.lower() == "q":
        quit()
    elif url.lower() == "dev":
        urls = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ","https://example.com/file1.txt",
        "https://example.com/file1.mp4","https://example.com/file1.mp3"]
        break
    elif url.lower() == "spotify":
        get_spotify_credentials()
    elif url.lower() == "help" or url.lower() == "commands":
        print(Fore.MAGENTA + "Here are the list of commands:\nq - Quit\nN - Finished\ndev - test if the program works\nspotify - enable spotify support if you disabled it")

    else:
        try:
            if "spotify" in url and Enabled == False:
                enter = input(Fore.RED + "Please enable Spotify support to use spotify songs.")
        
        except:
             enter = input(Fore.RED + "Please enable Spotify support to use spotify songs.")
            
        else:
            urls.append(url)
            print("-----------------------------------------------------------------------------")
            os.system("cls")

threads = []
for url in urls:
    filename = url.split("/")[-1]
    folder = 'DownloadedData'
    thread = Downloader(url,filename,folder)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
    elapsed_time = time.time() - start_time  # calculate the elapsed time for the entire script
    
print(Fore.LIGHTCYAN_EX + "-----------------------------------------------------------------------------")
print( Fore.LIGHTBLUE_EX +f"Finished downloading all files in " + Fore.LIGHTRED_EX + f"{elapsed_time:.2f} seconds.\n")

print(Style.RESET_ALL)
