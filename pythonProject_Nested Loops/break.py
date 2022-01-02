while True:
    try:
        print('Enter even number: ', end='')
        n=int(input())
        if n%2 == 0:
            print('Even number entered %d' % n)
            break
    except ValueError:
        print('Invalid number.')

