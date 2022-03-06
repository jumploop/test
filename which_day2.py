import datetime


def is_leap_year(year):
    """判断指定的年份是不是闰年，平年返回False，闰年返回True"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, day):
    """计算传入的日期是这一年的第几天"""
    end = datetime.date(year, month, day)
    start = datetime.date(year, 1, 1)
    return (end - start).days + 1


if __name__ == '__main__':
    today = datetime.datetime.today()
    print(today)
    print(which_day(today.year, today.month, today.day))
