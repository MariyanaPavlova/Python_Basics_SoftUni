budget = float(input())
n_videocard = int(input())
n_processor = int(input())
n_ram = int(input())

amount_videocard = n_videocard * 250
amount_processors = amount_videocard * 0.35
amount_ram = amount_videocard * 0.10
total = amount_videocard+(amount_processors*n_processor)+(amount_ram*n_ram)
if n_videocard > n_processor:
    total = total - total*0.15

diff = budget-total
if total <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(diff):.2f} leva more!")