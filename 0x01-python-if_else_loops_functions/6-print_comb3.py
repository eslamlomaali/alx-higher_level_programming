#!/usr/bin/python3
for n in range(0, 10):
    for o in range(n + 1, 10):
        if n == 8 and o == 9:
            print('89')
        else:
            print('{}{}, '.format(n, o), end='')
