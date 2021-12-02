exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

late = 'Late'
on_time = 'On time'
early = 'Early'
result = None

exam_time = (exam_hour * 60) + exam_min
arrival_time = (arrival_hour * 60) + arrival_min

total_min = arrival_time - exam_time
stud_arrival = late

if total_min < -30:
    stud_arrival = early
elif total_min <= 0:
    stud_arrival = on_time

if total_min != 0:
    hour_diff = abs(total_min) // 60
    min_diff = abs(total_min) % 60

    if hour_diff > 0:
        result = f'{hour_diff}:{min_diff:02} hours'
    else:
        result = f'{min_diff} minutes'

    if total_min < 0:
        result = result + ' before the start'
    else:
        result = result + ' after the start'
print(stud_arrival)
if result != None:
    print(result)
else:
    pass


