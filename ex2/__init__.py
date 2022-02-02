from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        def func_wrapper(*args, **kwargs):
            start_time = time.time()
            for i in range(num):
                iter_start_time = time.time()
                func(*args, **kwargs)
                print(time.time() - iter_start_time)
            print((time.time() - start_time) / num)
        return func_wrapper
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
