amount = int(input())
product = input()

counter = 1
successful_purches = 0
paid_card = 0
paid_cash = 0
card = 0
cash = 0

while product != 'End':
    product_i = int(product)

    if counter %2 == 0 and counter != 0:
        if product_i < 10:
            print(f'Error in transaction!')
        else:
            print(f'Product sold!')
            paid_cash += product_i
            cash += 1
            successful_purches += product_i
    else:
        if product_i > 100:
            print(f'Error in transaction!')
        else:
            print(f'Product sold!')
            paid_card += product_i
            card += 1
            successful_purches += product_i

    if successful_purches >= amount:
        sum_cash = paid_cash/cash
        sum_card = paid_card/card
        print(f'Average CS: {sum_card:.2f}')
        print(f'Average CC: {sum_cash:.2f}')
        break
    counter += 1
    product = input()
else:
    print(f'Failed to collect required money for charity.')
