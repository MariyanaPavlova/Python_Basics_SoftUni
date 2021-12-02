import math
hours=int(input())
days=int(input())
employees=int(input())

work_days = days - days*0.10
work_hours = math.floor(10 * work_days)
all_time=employees*work_hours

diff=abs(all_time-hours)

if all_time < hours:
    print(f'Not enough time!{diff} hours needed.')
else:
    print(f"Yes!{diff} hours left.")