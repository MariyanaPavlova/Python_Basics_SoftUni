import math
n=int(input())  #123

result1 = n % 10    # еденици
result10 = n // 10%10   # десетици
result100= n // 100%10     #стотици
result1000= n //1000    #хилядни

print(result1)
print(result10)
print(result100)
print(result1000)