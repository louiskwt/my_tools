import argparse, asyncio
import os
from bilix.sites.bilibili import DownloaderBilibili

parser = argparse.ArgumentParser(description="Download videos from Bilibili")
parser.add_argument("-v", "--video", help="Get a single video", type=str)
parser.add_argument("-s", "--series", help="Get a series", type=str)

os.makedirs("videos", exist_ok=True)

async def main():
    args = parser.parse_args()
    try:
        async with DownloaderBilibili() as d:
            d.progress.start()
            if args.video:
                await d.get_video(args.video, "videos")
            elif args.series:
                await d.get_series(args.series, "videos")
            else:
                parser.print_help()
    except Exception as e:
        print(f"Error when downloading: {e}")


if __name__ == '__main__':
    asyncio.run(main())