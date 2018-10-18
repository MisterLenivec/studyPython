# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.
# Sample Input 1:
# 2016 4 20
# 14
# Sample Output 1:
# 2016 5 4

# First solution
import datetime

(y, m, d) = [int(n) for n in input().split()]
date_now = datetime.date(y, m, d)
plus_day = datetime.timedelta(days=int(input()))
days_later = date_now + plus_day
print(days_later.strftime('%Y %-m %-d'))
# print(days_later.strftime('%Y %#m %#d')) # Для винды убираем нули из месяца и дня

# Second
from datetime import datetime, timedelta

y, m, d = map(int, input().split())
new_date = datetime(y, m, d) + timedelta(days=int(input()))
print('{d.year} {d.month} {d.day}'.format(d=new_date))
