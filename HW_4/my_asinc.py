import asyncio
import aiohttp
import time
import aiofiles


async def download(url):
    async with aiohttp.ClientSession() as session:
        name_file = url.split('/')[-1]
        start_time = time.time()
        async with session.get(url) as response:
            if response.status == 200:
                p = await aiofiles.open(name_file, mode='wb')
                await p.write(await response.read())
                await p.close()
            print(f'Время скачивания картинки {name_file} составило: {time.time() - start_time} сек.')


async def main(urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


def loop_asinc(urls):
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))
    print(f'Время выполнения программы составило: {time.time() - start_time} сек.')


if __name__ == '__main__':
    from main import urls
    loop_asinc(urls)