num = input()
num = reversed(num)

for digits in num:
    numb = int(digits)
    for i in range(numb):
        if numb != 0:
            symbol = chr(numb+33)
            print(symbol, end="")
    if numb == 0:
        print('ZERO')
    else:
        print()