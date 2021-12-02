price_trip = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minons = int(input())
count_tracks = int(input())

sum_count = count_puzzles + count_dolls + count_bears + count_minons + count_tracks
sum = count_puzzles * 2.60 + count_dolls * 3 + count_bears * 4.10 + count_minons * 8.20 + count_tracks * 2
if sum_count >= 50:
    discount = sum * 0.25
else:
    discount = 0
sum_total = sum - discount
naem = sum_total * 0.10
final_money = sum_total - naem
ff = abs(final_money - price_trip)
if final_money >= price_trip:
    print(f'Yes! {ff:.2f} lv left.')
else:
    print(f'Not enough money! {ff:.2f} lv needed.')
