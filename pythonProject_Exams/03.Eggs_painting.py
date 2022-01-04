size = input()
color = input()
partidi = int(input())

if color == 'Red':
    if size == 'Large':
        price = partidi *16
    elif size == 'Medium':
        price = partidi * 13
    elif size == 'Small':
        price = partidi * 9
elif color == 'Green':
    if size == 'Large':
        price = partidi *12
    elif size == 'Medium':
        price = partidi * 9
    elif size == 'Small':
        price = partidi * 8
elif color == 'Yellow':
    if size == 'Large':
        price = partidi *9
    elif size == 'Medium':
        price = partidi * 7
    elif size == 'Small':
        price = partidi * 5
price = price - price*0.35
print(f'{price:.2f} leva.')