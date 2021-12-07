t = int(input())
salary = int(input())

for i in range(t):
    site = str(input())
    if site == 'Facebook' and salary !=0:
        salary -= 150
    if site == 'Instagram' and salary !=0:
        salary -= 100
    if site == 'Reddit' and salary !=0:
        salary -= 50
    if salary == 0:
        print('You have lost your salary.')
        break
if salary > 0:
    print(salary)
