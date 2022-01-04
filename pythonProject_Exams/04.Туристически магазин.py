budget = float(input())

product = 0
count = 1
total_price = 0
budget_remain = 0

while True:
    item = input()
    if item == "Stop":
        print(f'You bought {count - 1} products for {total_price:.2f} leva.')
        break

    item_price = float(input())
    diff = budget_remain-item_price
    if item_price > budget_remain and budget_remain != 0:
        print("You don't have enough money!")
        print(f"You need {abs(diff):.2f} leva!")
        break
    if count % 3 ==0:
        item_price = item_price/2
    total_price += item_price
    budget_remain = budget-total_price
    count +=1

# граничната стойност budget remain 0 при изхарчване с пок.1
