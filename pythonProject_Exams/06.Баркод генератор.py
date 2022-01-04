a = int(input())
b = int(input())

a1 = a//1000
a2 = a%1000//100
a3 = a%100//10
a4 = a%10

b1 = b//1000
b2 = b%1000//100
b3 = b%100//10
b4 = b%10

for i1 in range(a1, b1+1):
    if i1 %2 !=0:
        i1=i1
    else:
        i1=0
    for i2 in range(a2, b2+1):
        if i2 %2 !=0:
            i2 =i2
        else:
            i2=0
        for i3 in range(a3, b3+1):
            if i3 %2 !=0:
                i3=i3
            else:
                i3=0
            for i4 in range(a4, b4+1):
                if i4 % 2 != 0:
                    i4=i4
                else:
                    i4=0
                if i4 !=0 and i3 !=0 and i2 !=0 and i1 !=0:
                    print(f'{i1}{i2}{i3}{i4} ', end='')
