actor = input()
first_points = float(input())
count = int(input())
total = first_points
points=0
diff=0
for i in range(count):
    name = input()
    points = float(input())
    lenth = len(name)
    summ = points*lenth/2
    total += summ
    diff = 1250.5-total
    if total >= 1250.5:
        print(f'Congratulations, {actor} got a nominee for leading role with {total:.1f}!')
        break
if total < 1250.5:
        print(f'Sorry, {actor} you need {diff:.1f} more!')
