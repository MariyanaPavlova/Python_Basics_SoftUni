capacity = int(input())

remain = capacity
price = 0

while remain >= 0:
    people_c = input()

    if people_c == 'Movie time!':
        print(f'There are {remain} seats left in the cinema.')
        print(f'Cinema income - {price} lv.')
        exit()

    people_count = int(people_c)

    if remain > 1:
        remain -= people_count
        if people_count % 3 ==0:
            price += (people_count *5 - 5)
        else:
            price += people_count *5
    else:
        break
print(f'The cinema is full.')
print(f'Cinema income - {price} lv.')
