count = int(input())
points=0
max=0
namee=0

for i in range(count):
    name = input()
    points = 0
    while True:
        grade = input()
        if grade == 'Stop':
            print(f'{name} has {points} points.')
            if namee ==name:
                print(f'{namee} is the new number 1!')
            break

        gradee=int(grade)
        points+=gradee
        if points>max:
            max=points
            namee=name
print(f'{namee} won competition with {max} points!')
