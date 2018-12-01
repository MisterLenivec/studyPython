# В этой задаче вам необходимо воспользоваться API сайта artsy.net
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
# выведите их имена в лексикографическом порядке.
# Примечание:
# ﻿В качестве имени художника используется параметр sortable_name в кодировке UTF-8.
# Пример входных данных:
# 4d8b92b34eb68a1b2c0003f4
# 537def3c139b21353f0006a6
# 4e2ed576477cc70001006f99
# Пример выходных данных:
# Abbott Mary
# Warhol Andy
# Abbas Hamra

import requests
import json

client_id = "It's a secret"
client_secret = "It's a secret too"
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]
headers = {"X-Xapp-Token": token}
d = {}

with open('dataset_24476_4 (6).txt', encoding="utf-8") as f, open('answer.txt', "w", encoding="utf-8") as w:
    lst = [line.strip() for line in f]
    for i in lst:
        r = requests.get("https://api.artsy.net/api/artists/" + str(i), headers=headers)
        j = json.loads(r.text)
        if (j['birthday'] in d):
            d[j['birthday']].append(j['sortable_name'])
        else:
            d[j['birthday']] = [j['sortable_name']]
    for key in sorted(d.keys()):
        for value in sorted(d[key]):
            w.write(value + '\n')
