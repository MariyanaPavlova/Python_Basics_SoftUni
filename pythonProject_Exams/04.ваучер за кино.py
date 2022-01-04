vaucher = int(input())
remaining_amount = 0
count_purchase = 0
count_tickets = 0

while True:
    purchase = input()
    if purchase == 'End':
        break
    purc = len(purchase)
    if purc > 8:
        a = purchase[0:1]
        b = purchase[1:2]
        a1 = ord(a)
        a2 = ord(b)
        c = a1 + a2
        if c <= vaucher:
            vaucher -= c
            count_tickets += 1
        else:
            print(f"{count_tickets}")
            print(f"{count_purchase}")
    else:
        aa = purchase[0:1]
        aa1 = ord(aa)
        cc = aa1
        if cc <= vaucher:
            vaucher -= cc
            count_purchase += 1
        else:
            break

print(f"{count_tickets}")
print(f"{count_purchase}")
