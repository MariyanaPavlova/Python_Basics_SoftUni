import sys
n=input()

min = sys.maxsize

while n != "Stop":
    curr = int(n)
    if curr < min:
        min = curr
    n = input()
print(min)