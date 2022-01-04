import math
count_break = int(input())
count_workers = int(input())
cart_limit = int(input())

bricks_course = count_workers * cart_limit
courses = math.ceil(count_break / bricks_course)

print(courses)