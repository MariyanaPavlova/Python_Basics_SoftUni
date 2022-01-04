import math

z=0
y=0
max=0
namee=None

while True:
    name = input()
    if name == 'End of words':
        break

    for i in range(0, len(name)):
        z += ord(name[i])

    if name[0:1] == 'a' or name[0:1] =='e' or name[0:1] =='i' or name[0:1] =='o' or name[0:1] =='u' or name[0:1] =='y':
        y= z*len(name)
    elif name[0:1] == 'A' or name[0:1] =='E' or name[0:1] =='I' or name[0:1] =='O' or name[0:1] =='U' or name[0:1] =='Y':
         y= z*len(name)
    else:
        y= math.floor(z/len(name))
    if y > max:
        max = y
        namee=name
    y = 0
    z = 0
print(f"The most powerful word is {namee} - {max}" )