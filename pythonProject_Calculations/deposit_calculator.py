deposit_amount = float(input())
deposit_time = int(input())
interest = float(input())

interest_amount = deposit_amount * interest/100
month_interest = interest_amount/12
sum = deposit_amount + (month_interest*deposit_time)
print(sum)

