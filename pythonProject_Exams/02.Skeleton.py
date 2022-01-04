min = int(input())
sec = int(input())
l = float(input())
m = int(input())
time=0

controla = min*60+sec
delay= l /120
delay_time = delay*2.5

time = ((l /100)*m)-delay_time
diff = abs(controla-time)
if time <=controla:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {time:.3f}.')
else:
    print(f'No, Marin failed! He was {diff:.3f} second slower.')
