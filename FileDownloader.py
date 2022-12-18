import threading
import requests
import os
import time
import pytube



def download_youtube_video(url, folder, filetype):
    from colorama import Fore, Style


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
            from colorama import Fore, Style


            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
            
            global start_time

            start_time = time.time()
        
            if "youtube" in self.url:
                filetype = "mp4"
                
                download_youtube_video(self.url, self.folder, filetype)
                return

            try:
                response = requests.get(self.url, stream=True) #Here we get request the data using requests.get, and inputing the url
                print(Fore.LIGHTMAGENTA_EX + f"{self.filename}"  + Fore.CYAN +  "is downloading...\n")
                print("-----------------------------------------------------------------------------")
            except:
                print(Fore.RED + f"The url inputed for {self.filename} is not a vaild type of url to download\n This file will not be downloaded and skipped.\n")
                return

            file_path = os.path.join(self.folder,self.filename)
            with open(file_path,"wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            end_time = time.time()  # record the end time
            elapsed_time = end_time - start_time  # calculate the elapsed time
            
            print(Fore.LIGHTMAGENTA_EX + f"{self.filename} has been downloaded in"  + Fore.LIGHTRED_EX + f"{elapsed_time:.2f} seconds.\n")


from colorama import Fore, Style
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
    else:
        urls.append(url)
        os.system("cls")
        print("-----------------------------------------------------------------------------")

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
