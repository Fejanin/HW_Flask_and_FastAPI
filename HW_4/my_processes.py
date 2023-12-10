import multiprocessing
import time
import requests


def get_picture(url):
    name_file = url.split('/')[-1]
    start_time = time.time()
    p = requests.get(url)
    with open(name_file, 'wb') as f:
        f.write(p.content)
    print(f'Время скачивания картинки {name_file} составило: {time.time() - start_time} сек.')


def loop_proc(urls):
    start_time = time.time()
    processes = []
    for url in urls:
        p = multiprocessing.Process(target=get_picture, args=(url,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print(f'Время выполнения программы составило: {time.time() - start_time} сек.')



if __name__ == '__main__':
    from main import urls
    loop_proc(urls)