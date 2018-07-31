# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
# слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько,
# вывести лексикографически первое (можно использовать оператор < для строк).
# Слова, написанные в разных регистрах, считаются одинаковыми.
with open('dataset_3363_3.txt') as inf:
    a = inf.read().replace('\n', ' ').lower().split()
# a = ['zy', 'zy', 'abtdd', 'zy', 'yxzux', 'zy', 'adzx', 'zuaux', 'zy', 'xacpptxcp', 'pcb', 'zy', 'pyaccxpb', 'zuaux', 'ap', 'cbaupcc', 'zy', 'yd', 'tup', 'pa', 'uzaaa', 'duxtx', 'tbzz', 'zy', 'zy', 'zuuaybau', 'ttz', 'au', 'cyu', 'yaxybcxp', 'dzudxcy', 'xc', 'uyxxd', 'au', 'tad', 'yaxybcxp', 'cxzdpy', 'zuuaybau', 'ptt', 'pcatacd', 'cxzdd', 'ycpctb', 'dxyzz', 'zuuaybau', 'c', 'aap', 'ubbucpctt', 'tpppu', 'au', 'x', 'zpbutct', 'zuuaybau', 'zuuaybau', 'ycpctb', 'apc', 'ppaaucb', 'tdbuxct', 'dzczx', 'pa', 'paapptddt', 'xtpdayy', 'tdtuuydu', 'uybxx', 'zuuaybau', 'xc', 'zxcyc', 'zuuaybau', 'pbtu', 'cxzdd', 'xuyxdzz', 'tdtuuydu', 'a', 'a', 'txyctcdpa', 'a', 'txyctcdpa', 'ab', 'attcct', 'utda', 'xz', 'uuct', 'yax', 'xt', 'czd', 'czd', 'ct', 'uuct', 'yax', 'ztaz', 'uxcztyupu', 'uu', 'a', 'ycbtdcpyb', 'yzctbpucy', 'yydydb', 'zxpcctabb', 'acut', 'adytxxup', 'adytxxup', 'a', 'adytxxup', 'uzdcdp', 'zy', 'uxz', 'a', 'z', 'bdbc', 'auubdyab', 'a', 'tcax', 'ddpbaauuz', 'a', 'zy', 'uzxzatbyu', 'td', 'uupx', 'z', 'puuycpybx', 'dd', 'uxz', 'buxx', 'd', 'z', 'cbypbb', 'uzdcdp', 'ztddct', 'xaxuactc', 'xdxy', 'xpayp', 'zxdxt', 'pcdc', 'ztddct', 'uxz', 'tcdbpzby', 'c', 'bdbc', 'tybtxa', 'ddpby', 'ddyczz', 'uzdcdp', 'auubdyab', 'xzy', 'ztddct', 'adytxxup', 'tdtzxcpt', 'atucc', 'a', 'bcdu', 'ydtubput', 'tb', 'cazdca', 'tb', 'x', 'zaub', 'c', 'xdbxxy', 'pc', 'xxpczxtab', 'xxpczxtab', 'dbzt', 'xxpczxtab', 'xbyyp', 'xbyyp', 'dbzt', 'xxpczxtab', 'pcp', 'xtuzd', 'cpu', 'pc', 'yupyuzbdd', 'xxpczxtab', 'xxpczxtab', 'ztxybptdc', 'zapbytztz', 'ypuyp', 'yupyuzbdd', 'aypyc', 'cytptctzb', 'xxpczxtab', 'cpu', 'zacu', 'xdu', 'uu', 'dtbutuzdu', 'xyu', 'dtbutuzdu', 'z', 'ycaaxbx', 'bzpuccbcp', 'papucbp', 'ppubd', 'p', 'bxcaxt', 'x']
s = set(a)
counter = 0
word = a[0]
for x in s:
    if (counter < a.count(x)):
        counter = a.count(x)
        word = x
    if (counter == a.count(x)):
        if (x < word):
            word = x

result = word + ' ' + str(counter)
# print(result)
# print(a)

with open('dataset_3363_3.txt', 'w') as ouf:
    ouf.write(str(result))
