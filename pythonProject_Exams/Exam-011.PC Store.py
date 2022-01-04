pros=float(input())
video = float(input())
ram = float(input())
count_ram = int(input())
perc = float(input())

price_pros_lv = pros*1.57
price_video_lv= video*1.57
price_ram = ram *1.57
all_price_ram = price_ram*count_ram
disc_pros = price_pros_lv-price_pros_lv*perc
disc_video = price_video_lv-price_video_lv*perc

total = disc_video+disc_pros+all_price_ram
print(f'Money needed - {total:.2f} leva.')

