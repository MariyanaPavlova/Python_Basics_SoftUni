budget = float(input())
name = input()
total = budget
salary=0

while name != 'ACTION':

    if len(name) <= 15:
        honorar = float(input())
        total -= honorar
    else:
        honorar = total * 0.20
        total -= honorar

    if total < 0:
        print(f'We need {abs(total):.2f} leva for our actors.')
        break
    name = input()

if total >= 0:
    print(f'We are left with {abs(total):.2f} leva.')