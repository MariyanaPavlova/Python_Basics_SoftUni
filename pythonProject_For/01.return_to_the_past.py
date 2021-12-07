heritage=float(input())
years_live=int(input())
years=18
rem_money=heritage

for curr_year in range(1800,years_live+1):
    if curr_year %2==0:
        heritage -= 12000
    else:
        heritage -=(12000+50*years)
    years +=1

if heritage >=0:
    print(f'Yes! He will live a carefree life and will have {heritage:.2f} dollars left.')
else:
    print(f'He will need {abs(heritage):.2f} dollars to survive.')