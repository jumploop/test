from collections import Counter

import random


def count_letters(items):
    result = {}
    for item in items:
        if isinstance(item, (int, float)):
            result[item] = result.get(item, 0) + 1
    return result


print(count_letters([random.randint(0, 100) for _ in range(10)]))


def count_letters(items):
    counter = Counter(items)
    return {
        key: value
        for key, value in counter.items() if isinstance(key, (int, float))
    }


print(count_letters([random.randint(0, 100) for _ in range(10)]))


