n = int(input())
counter=0
for x1 in range(1, n+1):
    for x2 in range(1, n+1):
        for x3 in range(1, n+1):
            for x4 in range(1, n+1):
                for x5 in range(1, n+1):
                    for x6 in range(1, n+1):
                        if x1*x2*x3*x4*x5*x6 == n:
                            print(f'{x1}{x2}{x3}{x4}{x5}{x6} ', end='')
