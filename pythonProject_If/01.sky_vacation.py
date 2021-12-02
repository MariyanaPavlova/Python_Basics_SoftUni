days = int(input())
room = input()
mark = input()
discount = 0
prize = 0
nights = days - 1

if nights < 10:
    if room == 'room for one person':
        prize = 18.00 * nights
    elif room == 'apartment':
        prize = (25 - (25 * 0.30)) * nights
    elif room == 'president apartment':
        prize = (35 - (35 * 0.10)) * nights

elif 10 <= nights <= 15:
    if room == 'room for one person':
        prize = 18.00 * nights
    elif room == 'apartment':
        prize = (25 - (25 * 0.35)) * nights
    elif room == 'president apartment':
        prize = (35 - (35 * 0.15)) * nights
elif nights > 15:
    if room == 'room for one person':
        prize = 18.00 * nights
    elif room == 'apartment':
        prize = (25 - (25 * 0.50)) * nights
    elif room == 'president apartment':
        prize = (35 - (35 * 0.20)) * nights
if mark == 'positive':
    prize = prize + prize * 0.25
elif mark == 'negative':
    prize = prize - prize * 0.10
print(f'{prize:.2f}')
