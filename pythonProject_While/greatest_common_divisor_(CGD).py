a = int(input())
b = int(input())

while b != 0:
    b1 = b
    b = a % b
    a = b1
print(f'GCD = {a}')