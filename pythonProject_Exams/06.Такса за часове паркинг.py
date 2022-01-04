days = int(input())
hours = int(input())
tax = 0
tax_tot = 0

for i in range(1, days+1):

    tax = 0
    for ih in range(1, hours+1):
        if i % 2 == 0 and ih % 2 != 0:
            tax += 2.5
        elif i % 2 != 0 and ih % 2 == 0:
            tax += 1.25
        else:
            tax += 1
    tax_tot += tax
    print(f'Day: {i} - {tax:.2f} leva')
print(f'Total: {tax_tot:.2f} leva')