x1 = float(input())
y1 = float(input())
x2= float(input())
y2 = float(input())

wigth = abs(x1-x2)
height = abs(y1 - y2)

area = wigth * height
perimeter = 2 * wigth + 2 * height

print(f'{area:.2f}')
print(f'{perimeter:.2f}')
