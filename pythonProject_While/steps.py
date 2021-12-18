count_steps=0

while count_steps < 10000:
    steps = input()

    if steps == 'Going home':
        steps2 = int(input())
        count_steps += steps2
        diff = abs(10000-count_steps)
        if count_steps < 10000:
            print(f'{diff} more steps to reach goal.')
            break
    else:
        stepss = int(steps)
        count_steps += stepss
        diff = abs(10000-count_steps)
else:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')

