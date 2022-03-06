import datetime


def is_leap_year(year):
    """判断指定的年份是不是闰年，平年返回False，闰年返回True"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, day):
    """计算传入的日期是这一年的第几天"""
    # 用嵌套的列表保存平年和闰年每个月的天数
    days_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    days = days_of_month[is_leap_year(year)][:month - 1]
    return sum(days) + day


if __name__ == '__main__':
    today = datetime.date.today()
    print(today)
    print(which_day(today.year, today.month, today.day))
