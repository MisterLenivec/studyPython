from sys import argv

#first solution
print(*argv[1:])

#second
print(' '.join(argv[1:]))

#third
for i in range(1, len(argv)):
    print(argv[i], end = ' ')

#fourth
for i in argv[1:]:
    print(i, end = ' ')