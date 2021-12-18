n = input()
total = 0

while n != 'NoMoreMoney':

    curr = float(n)
    if curr < 0:
        print('Invalid operation!')
        break
    else:
        print(f'Increase: {curr:.2f}')
        total += curr
    n = input()

print(f'Total: {total:.2f}')
