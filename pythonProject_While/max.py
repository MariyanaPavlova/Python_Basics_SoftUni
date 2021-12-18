import sys
n = input()
maxx = - sys.maxsize

while n != 'Stop':
    curr = int(n)
    if curr > maxx:
        maxx = curr
    n = input()
print(maxx)