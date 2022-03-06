from functools import lru_cache


@lru_cache()
def change_money(total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    return change_money(total - 2) + change_money(total -
                                                  3) + change_money(total - 5)


print(change_money(99))