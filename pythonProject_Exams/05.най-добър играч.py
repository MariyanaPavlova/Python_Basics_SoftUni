best=0
current=0
best_name=0
het_trick=0
gols=0
while not gols >= 10:
    name = input()
    if name == 'END':
        break
    count_gols = int(input())
    gols=count_gols

    current = count_gols
    if current > best:
        best=current
        best_name=name
    elif current==best:
        pass
    if count_gols >= 3:
        het_trick=count_gols

if het_trick >=3:
    print(f'{best_name} is the best player!')
    print(f'He has scored {best} goals and made a hat-trick !!!')

else:
    print(f'{best_name} is the best player!')
    print(f'He has scored {best} goals.')