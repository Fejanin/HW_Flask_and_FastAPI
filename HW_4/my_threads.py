import threading
import time
import requests


def get_picture(url):
    name_file = url.split('/')[-1]
    start_time = time.time()
    p = requests.get(url)
    with open(name_file, 'wb') as f:
        f.write(p.content)
    print(f'Время скачивания картинки {name_file} составило: {time.time() - start_time} сек.')


def loop_threads(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        t = threading.Thread(target=get_picture, args=(url,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f'Время выполнения программы составило: {time.time() - start_time} сек.')



if __name__ == '__main__':
    from main import urls
    loop_threads(urls)
