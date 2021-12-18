max_bad_grades = int(input())

bad_grades_counts = 0
total = 0
problems_count = 0
last_problem = None

while bad_grades_counts < max_bad_grades:
    problem = input()
    if problem == "Enough":
        break
    grade = int(input())
    if grade <= 4:
        bad_grades_counts += 1

    total += grade
    problems_count += 1
    last_problem = problem

if bad_grades_counts == max_bad_grades:
    print(f'You need a break, {bad_grades_counts} poor grades.')
else:
    average=total/problems_count
    print(f'Average score: {average:.2f}')
    print(f'Number of problems: {problems_count}')
    print(f'Last problem: {last_problem}')