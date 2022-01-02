n=int(input())
prime=0

for i in range(2, n+1):
    if n%i ==0 and n%2!= 0 or n >= 2:
        prime=i
        break
    else:
        prime=0
if prime != 0:
    print('Prime')

else:
     print('Not prime')