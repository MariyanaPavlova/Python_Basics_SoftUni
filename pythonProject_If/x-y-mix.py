x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
x=float(input())
y=float(input())

first_cond = x==x1 or x==x2
second_cond = y==y1 or y==y2
inside = y1<=y<=y2 and x1<=x<=x2

#if x>=x1 and x<=x2 and y>=y1 and y<=y2:
    #print('Inside / Outside')

if x1<=y<=y2 and x1<=x<=x2:
    print('Inside / Outside')

elif first_cond or second_cond:
    print('Border')

else:
    print('Inside / Outside')