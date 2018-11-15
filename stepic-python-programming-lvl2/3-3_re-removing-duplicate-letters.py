# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'(\w)\1+', r'\1', line))
