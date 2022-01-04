count = int(input())
buy = input()
selled = count
only_selled=0

while buy != 'Close':
    add = input()
    if buy == 'Buy':
        if int(add) > selled:
            print(f'Not enough eggs in store!')
            print(f'You can buy only {selled}.')
            exit()
        else:
            selled -= int(add)
            only_selled += int(add)
    elif buy == 'Fill':
        selled += int(add)

    buy = input()

print(f"Store is closed!")
print(f'{only_selled} eggs sold.')