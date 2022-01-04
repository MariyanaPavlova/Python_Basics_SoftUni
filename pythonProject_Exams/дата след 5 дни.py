dayy = input()
monthh = input()

if monthh == '2' or monthh == '02':
    day = int(dayy)
    monthhh = int(monthh)
    day += 5

    if day > 28:
        monthhh += 1
        s = 28 - day

elif monthh == '04' or monthh == '4' or monthh == '06' or monthh == '6' or monthh == '09' or monthh == '9' or monthh == '11':
    day = int(dayy)
    monthhh = int(monthh)
    day += 5

    if day > 30:
        monthhh += 1
        s = 30 - day
else:
    day = int(dayy)
    monthhh = int(monthh)
    day += 5
    s = day

    if day > 31:
        monthhh += 1
        s = 31 - day
if monthhh > 12:
    monthhh = 1
if monthhh <= 9:
    print(f'{abs(s)}.0{monthhh}')
else:
    print(f'{abs(s)}.{monthhh}')