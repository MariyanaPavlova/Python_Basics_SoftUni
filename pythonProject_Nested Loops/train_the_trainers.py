n = int(input())
sum_all_grade = 0
grade_count = 0

while True:
    name = input()
    if name == 'Finish':
        break
    sum_grade = 0

    for i in range(n):
        grade = float(input())
        sum_grade += grade
        grade_count +=1
        sum_all_grade += grade

    aver_grade = sum_grade / n
    print(f'{name} - {aver_grade:.2f}.')

sum_aver_grade = sum_all_grade / grade_count
print(f"Student's final assessment is {sum_aver_grade:.2f}.")
