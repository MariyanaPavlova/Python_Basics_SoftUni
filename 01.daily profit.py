working_day_month = int(input())
earned_money_per_day = float(input())
currency = float(input())

monthly_salary = working_day_month * earned_money_per_day
earned_money_year = monthly_salary * 12 + monthly_salary * 2.5
taxes = earned_money_year * 0.25
net_amount_usd = earned_money_year - taxes
net_amount_bgn = net_amount_usd * currency
net_eared_per_day = net_amount_bgn / 365

print("%.2f"% net_eared_per_day)
#print(f'{net_eared_per_day:.2f}')