from pytubefix import YouTube

def download(link):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    try: 
        yt.download()
        print("Download Completed")
    except Exception as e:
        print(f"Failed to download due to error: {e}")
  
def main():
    url = input('Enter the url: ')
    download(url)

if __name__ == "__main__":
    main()