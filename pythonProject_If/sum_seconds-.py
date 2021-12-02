a=int(input())
b=int(input())
c=int(input())

time=a+b+c
min = time//60
sec = time%60
if sec<10:
    print(f'{min}:0{sec}')
else:
    print(f'{min}:{sec}')
