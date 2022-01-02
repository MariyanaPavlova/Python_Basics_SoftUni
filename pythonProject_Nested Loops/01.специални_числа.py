n=int(input())

for x1 in range(1, 9+1):
    if n % x1 == 0:
        s1=x1
    else:
        s1=0
    for x2 in range(1, 9+1):
        if n % x2 == 0:
            s2=x2
        else:
            s2=0
        for x3 in range(1, 9+1):
            if n % x3 == 0:
                s3=x3
            else:
                s3=0
            for x4 in range(1, 9+1):
                if n % x4 == 0:
                    s4=x4
                else:
                    s4=0
                if s1!=0 and s2!=0 and s3!=0 and s4!=0:
                    print(f'{s1}{s2}{s3}{s4} ', end='')
                else:
                    pass

