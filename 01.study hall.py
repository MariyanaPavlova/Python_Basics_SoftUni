width = float(input())
height = float(input())

width_cm = width*100
height_cm = height*100

width_cm = width_cm//120
height_cm = (height_cm -100)//70
buros= width_cm * height_cm - 3
print(buros)

