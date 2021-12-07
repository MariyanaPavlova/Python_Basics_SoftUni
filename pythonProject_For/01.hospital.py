period = int(input())
treated_patients=0
untreated_patients=0
count_doctors=7

for day in range(1,period+1):
    curr_patients=int(input())

    if day %3 ==0 and (untreated_patients > treated_patients):
        count_doctors +=1

    if curr_patients > count_doctors:
        treated_patients += count_doctors
        untreated_patients += curr_patients - count_doctors
    else:
        treated_patients += curr_patients

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
