
while True:
    try:
        n = int(input())
        if n%2 == 0:
            break
        print(f'Even number entered: {n}')
    except ValueError:
        print('Invalid number.')
