import asyncio
from bilix.sites.bilibili import DownloaderBilibili

async def main():
    url = input("Enter a series to download: ")
    async with DownloaderBilibili() as d:
        await d.get_series(url, "./videos")


if __name__ == '__main__':
    asyncio.run(main())