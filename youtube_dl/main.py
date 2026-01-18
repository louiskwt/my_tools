from pytubefix import YouTube
from pytubefix.cli import on_progress

def download(link):
    yt = YouTube(link, on_progress_callback=on_progress)
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