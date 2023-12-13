import sys
from my_threads import loop_threads
from my_processes import loop_proc
from my_asinc import loop_asinc


# тестовые данные
urls = [
    'https://ts2.space/wp-content/uploads/2023/10/What-is-the-purpose-of-robots_65308fe40fadb.jpg',
    'https://cff2.earth.com/uploads/2023/06/11162528/Robot-2.jpg',
    'https://media.newyorker.com/photos/59097c0b8b51cf59fc423d8f/master/pass/161128_r29058.jpg',
    'https://voonze.com/wp-content/uploads/2023/05/robot-parpadear.jpg',
    'https://img.freepik.com/premium-photo/macro-view-of-a-quirky-robotic-bug-ai-generative_972163-1594.jpg'
]


def main():
    try:
        flag, *urls = sys.argv[1:]
        if flag == 't':
            loop_threads(urls)
        elif flag == 'p':
            loop_proc(urls)
        elif flag == 'a':
            loop_asinc(urls)
        else:
            print('Вы не указали флаг для обработки данных (флаги: t, p, a) перед ссылками.')
    except ValueError:
        print('Вы не передали аргументов для работы программы.\nПример: python main.py t https://cff2.earth.com/uploads/2023/06/11162528/Robot-2.jpg')


if __name__ == '__main__':
    main()