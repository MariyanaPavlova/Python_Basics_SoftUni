age = float(input())
gender = input().lower()
pr = 0

if gender == 'f':
    if age < 16:
        p = 'Miss'
    else:
        p = 'Ms.'
else:
    if age < 16:
        p = 'Master'
    else:
        p = 'Mr.'
print(p)
