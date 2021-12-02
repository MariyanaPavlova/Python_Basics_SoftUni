a = int(input())

if a <= 100:
    tochki = 5
elif a > 100 and a < 1000:
    tochki = a * 0.2
else:
    tochki = a * 0.1
if a % 2 == 0:
    tochki = tochki + 1
if a % 10 == 5:
    tochki = tochki + 2
print(tochki)
print(a + tochki)
