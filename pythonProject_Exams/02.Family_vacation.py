burdget = float(input())
nights = int(input())
price = float(input())
add = int(input())


if nights > 7:
    sleep = price-price*0.05
    hotel = sleep*nights
else:
    hotel = price*nights
additional = burdget*add/100
sum = hotel+additional

diff = abs(burdget-sum)
if sum <= burdget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f'{diff:.2f} leva needed.')