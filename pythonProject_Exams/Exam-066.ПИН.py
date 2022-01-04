a = int(input())
b = int(input())
c = int(input())
count=0
for x1 in range(1, a+1):
    if x1 %2 ==0:
        s1=x1
    else:
        s1=0
    for x2 in range(2, b+1):
        if x2 ==2 or x2==3 or x2==5 or x2==7:
            s2=x2
        else:
            s2=0
        for x3 in range(1, c+1):
            if x3 %2 ==0:
                s3=x3
            else:
                s3=0
            if s1 != 0 and s2 != 0 and s3 != 0:
                print(f'{s1} {s2} {s3}')