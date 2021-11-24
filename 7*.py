price_strawberris = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_raspberries = float(input())
kg_strawberries = float(input())

price_raspberries = price_strawberris / 2
price_oranges = price_raspberries - price_raspberries * 0.40
price_bananas = price_raspberries - price_raspberries * 0.80

sum = kg_strawberries * price_strawberris + kg_bananas * price_bananas + kg_oranges * price_oranges + kg_raspberries * price_raspberries
print(sum)
