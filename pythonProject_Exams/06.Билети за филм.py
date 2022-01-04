a1 = int(input())
a2 = int(input())
n = int(input())
nn = int(n/2)
summ=0

for x1 in range(a1, a2):
    if x1 %2 !=0:
        ss = x1
        s1=chr(x1)
    else:
        s1=0
    for x2 in range(1, n):
        if x2 %2 !=0:
            s2 = x2
            summ+=s2
        else:
            s2=0
        for x3 in range(1, n-2):
            if x3 % 2 != 0:
                s3 = x3
                summ+=s3
            else:
                s3=0
            for x4 in range(a1, a2):
                if x4 % 2 != 0:
                    s4 = x4
                    summ+=s4
                else:
                    s4=0

                if s1!=0 and s2!=0 and s3!=0 and s4!=0 and ss==s4:
                    if (s2+s3+s4) %2!=0:
                        print(f'{s1}-{s2}{s3}{s4}', end='')
                        print()