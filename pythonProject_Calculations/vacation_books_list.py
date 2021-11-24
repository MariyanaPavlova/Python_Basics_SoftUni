pages_count = int(input())
pages_per_hour = int(input())
days_count = int(input())

total_hours = pages_count/pages_per_hour
needed_time = total_hours / days_count
print(needed_time)