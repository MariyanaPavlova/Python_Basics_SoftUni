days = int(input())
inp = ''
win = 0
win_count = 0
lose_count = 0
win_day = 0
win_count1 = 0
lose_count1 = 0
for i in range(days):

    while True:
        sport = input()
        if sport == 'Finish':
            if win_count > lose_count:
                win_day += (win + win * 0.10)
            else:
                win_day += win
            win = 0
            win_count = 0
            lose_count = 0
            break
        result = input()
        if result == 'win':
            win += 20
            win_count += 1
            win_count1 += 1
        elif result == 'lose':
            win += 0
            lose_count += 1
            lose_count1 += 1
if win_count1 > lose_count1:
    win_day = win_day + win_day * 0.20
    print(f"You won the tournament! Total raised money: {win_day:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {win_day:.2f}")
