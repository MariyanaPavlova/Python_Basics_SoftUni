budget = float(input())
count_stat = int(input())
prize_cloth_one = float(input())

sum_decor = budget * 0.10
if count_stat > 150:
    sum_prize_cloth = (count_stat*prize_cloth_one)-(count_stat*prize_cloth_one)*0.10

else:
    sum_prize_cloth = prize_cloth_one * count_stat

sum_film = sum_decor + sum_prize_cloth
remaining_sum = abs(budget - sum_film)

if sum_film > budget:
    print('Not enough money!')
    print(f"Wingard needs {remaining_sum:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {remaining_sum:.2f} leva left.")

