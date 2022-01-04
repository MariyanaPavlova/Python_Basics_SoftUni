name = input()
sum = 0
win = 0
max = -100000000000000000
nameee = ''

while name != 'Stop':
    sum =0

    for i in name:
        n = int(input())
        a = ord(i)
        if n == a:
            sum += 10
        else:
            sum += 2

    if sum > max:
        max = sum
        nameee = name
    elif sum == max:
        nameee=name
    name = input()
print(f"The winner is {nameee} with {max} points!")