# First solution - без проверки на отсутствующие данные
d = {str(a):[] for a in range(1, 12)}
with open('dataset_3380_5.txt') as inf:
    for line in inf:
        a = line.strip().split()
        d[a[0]].append(int(a[2]))

with open('dataset_3380_5.txt', 'w') as ouf:
    for keys, values in d.items():
        if (d[keys]):
            d[keys] = sum(values) / len(values)
            ouf.write(str(keys) + ' ' + str(d[keys]))
            ouf.write('\n')
        else:
            ouf.write(str(keys + ' ' + '-'))
            ouf.write('\n')