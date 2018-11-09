# Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть
# хотя бы один файл с расширением ".py".
# Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

import os

abc = set()
os.chdir("main")

abc = {current_dir[2:] for current_dir, dirs, files in os.walk(".") for file in files if (file.endswith('.py'))}
# for current_dir, dirs, files in os.walk("."):
#     for file in files:
#         if (file.endswith('.py')):
#             abc.add(current_dir[2:])

with open("main.txt", "w") as w:
    line = [i.strip() for i in sorted(abc)]
    line = "\n".join(line)
    w.write(line)
