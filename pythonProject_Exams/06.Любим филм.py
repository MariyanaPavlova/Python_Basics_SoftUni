z=0
sum=0
max=0
namee=None
count=0

while True:
    count +=1
    if sum > max:
        max = sum
        namee=name
    sum = 0
    name = input()
    if name == 'STOP':
        print(f'The best movie for you is {namee} with {max} ASCII sum.')
        break

    for i in name:

        z = ord(i)
        sum += z
        if 97 <= z <= 122:
            sum -= len(name) * 2
        if 65 <= z <= 90:
            sum-=len(name)
    if count ==7:
        print(f'The limit is reached.')
        print(f'The best movie for you is {namee} with {max} ASCII sum.')
        break
