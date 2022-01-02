comand = input()
prime_sum = 0
not_prime_sum = 0

while comand != 'stop':
    num = int(comand)
    counter = 0
    if num < 0:
        print('Number is negative.')
    else:
        for i in range(1, num+1):
            if num % i == 0:
                counter += 1
        if counter == 2:
            prime_sum += num
        else:
            not_prime_sum += num

    comand = input()
print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {not_prime_sum}')

