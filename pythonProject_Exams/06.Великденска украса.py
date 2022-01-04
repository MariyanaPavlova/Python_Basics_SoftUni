count= int(input())

ithem=0
price = 0
price_all=0

for i in range(count):

    ithem = 0
    price = 0
    while True:
        product = input()

        if product == 'Finish':

            if ithem %2 == 0:
                price =price - price*0.20
            price_all += price
            print(f'You purchased {ithem} items for {price:.2f} leva.')
            break
        ithem+=1

        if product == 'basket':
            price += 1.50
        elif product == 'wreath':
            price += 3.80
        elif product == 'chocolate bunny':
            price += 7

aver = price_all/count
print(f'Average bill per client is: {aver:.2f} leva.')