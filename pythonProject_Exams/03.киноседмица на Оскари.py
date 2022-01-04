film_name = input()
tipe_room = input()
count_ticket = int(input())

if tipe_room == 'normal':
    if film_name == 'A Star Is Born':
        price_ticket = 7.50
    elif film_name == 'Bohemian Rhapsody':
        price_ticket = 7.35
    elif film_name == 'Green Book':
        price_ticket = 8.15
    elif film_name == 'The Favourite':
        price_ticket = 8.75

elif tipe_room == 'luxury':
    if film_name == 'A Star Is Born':
        price_ticket = 10.50
    elif film_name == 'Bohemian Rhapsody':
        price_ticket = 9.45
    elif film_name == 'Green Book':
        price_ticket = 10.25
    elif film_name == 'The Favourite':
        price_ticket = 11.55

elif tipe_room == 'ultra luxury':
    if film_name == 'A Star Is Born':
        price_ticket = 13.50
    elif film_name == 'Bohemian Rhapsody':
        price_ticket = 12.75
    elif film_name == 'Green Book':
        price_ticket = 13.25
    elif film_name == 'The Favourite':
        price_ticket = 13.95
prihodi = count_ticket * price_ticket

print(f'{film_name} -> {prihodi:.2f} lv.')
