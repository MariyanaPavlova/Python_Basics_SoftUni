import math

record = float(input())
distance = float(input())
time = float(input())

dist_time = distance * time
delay = math.floor(distance / 50)
delay_time = delay*30
all_time = dist_time + delay_time
diff = all_time - record
if all_time < record:
    print(f"Yes! The new record is {all_time:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")
