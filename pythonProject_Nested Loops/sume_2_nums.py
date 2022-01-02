a = int(input())
b = int(input())
spec_num = int(input())
counter=0
counter_m=0

for x1 in range(a, b+1):
    for x2 in range(a, b+1):
        counter += 1
        if x1 + x2 == spec_num:
            counter_m = counter
            print(f'Combination N:{counter_m} ({x1} + {x2} = {spec_num})')
            exit()
print(f"{counter} combinations - neither equals {spec_num}")