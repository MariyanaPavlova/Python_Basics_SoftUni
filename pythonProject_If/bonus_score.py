a = int(input())
if a <= 100:
    bonus = 5
elif a > 100 and a < 1000:
    bonus = a * 0.2
elif a > 1000:
    bonus = a * 0.1
if a % 2 == 0:
    bonus_t = 1 + bonus
elif a % 10 == 5:
    bonus_t = 2 + bonus
else:
    bonus_t = 0 + bonus
tot = bonus_t
total = a + tot
print(tot)
print(total)
