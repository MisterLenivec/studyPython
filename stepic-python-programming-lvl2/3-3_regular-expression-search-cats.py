# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if (re.search(r"cat.*cat", line)):
        print(line)

# r"(.*cat.*){2,}"
# r"(cat).*\1"
