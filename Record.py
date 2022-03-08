from functools import wraps
import time


class Record:
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print(f'{func.__name__} 执行时间：{time.time()-start}秒')
            return result

        return wrapper


@Record()
def foo():
    print('foo')


if __name__ == '__main__':
    foo()
