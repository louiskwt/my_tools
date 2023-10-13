from pytube import YouTube


def download(link):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    try: 
        yt.download()
        print("Download Completed")
    except:
        print("Failed")
  
def main():
    url = input('Enter your the url: ')
    download(url)

main()