from functools import wraps
import time


def record_time(output):
    """可以参数化的装饰器"""

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            output(func.__name__, time.time() - start)
            return result

        return wrapper

    return decorate


@record_time(print)
def foo():
    print('foo')


if __name__ == '__main__':
    foo()
