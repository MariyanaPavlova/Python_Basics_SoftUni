group_count = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for i in range(1, group_count+1):
    climbers_count = int(input())

    if climbers_count <= 5:
        musala += climbers_count
    elif 6 <= climbers_count <= 12:
        monblan += climbers_count
    elif 13 <= climbers_count <= 25:
        kilimandjaro += climbers_count
    elif 26 <= climbers_count <= 40:
        k2 += climbers_count
    elif climbers_count > 40:
        everest += climbers_count

all_climbers = musala+monblan+kilimandjaro+k2+everest
percent_musala = musala/all_climbers*100
percent_monblan = monblan/all_climbers*100
percent_kilimandjaro = kilimandjaro/all_climbers*100
percent_k2 = k2/all_climbers*100
percent_everest = everest/all_climbers*100
print(f'{percent_musala:.2f}%')
print(f'{percent_monblan:.2f}%')
print(f'{percent_kilimandjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')
