price_kg_veg = float(input())
price_kg_fruit = float(input())
sum_kg_veg = int(input())
sum_kg_fruit = int(input())

vegetables = price_kg_veg * sum_kg_veg
fruit = price_kg_fruit * sum_kg_fruit
sum_bgn = vegetables + fruit
sum_eur = sum_bgn / 1.94

print(sum_eur)
