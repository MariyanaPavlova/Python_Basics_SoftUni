time = int(input())
scena = int(input())
time_scena = int(input())

snimki = scena * time_scena
teren = time*0.15
all_time = snimki+teren
diff = abs(time-all_time)
if all_time > time:
    print(f'Time is up! To complete the movie you need {round(diff)} minutes.')
else:
    print(f'You managed to finish the movie on time! You have {round(diff)} minutes left!')