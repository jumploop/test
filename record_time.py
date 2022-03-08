from functools import wraps
import time


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__} 执行时间: {time.time() - start}秒 ')
        return result

    return wrapper


@record_time
def foo():
    print('hello world')


if __name__ == '__main__':
    foo()