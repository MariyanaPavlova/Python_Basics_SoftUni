rent_room = int(input())

statue = rent_room - rent_room*0.30
ketering = statue - statue * 0.15
sound = ketering/2
sum = rent_room + statue + ketering + sound

print(f'{sum:.2f}')
