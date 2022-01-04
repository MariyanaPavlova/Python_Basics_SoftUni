first = int(input())
second = int(input())
comand = input()

while comand != 'End of battle':
    if comand == 'one':
        second-=1
    elif comand == 'two':
        first-=1

    if first <=0:
        print(f'Player one is out of eggs. Player two has {second} eggs left.')
        break
    elif second <=0:
        print(f'Player two is out of eggs. Player one has {first} eggs left.')
        break
    comand=input()
if first >0 and second >0:
    print(f'Player one has {first} eggs left.')
    print(f'Player two has {second} eggs left.')