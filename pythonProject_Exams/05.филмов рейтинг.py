films = int(input())
average = 0
reiting=0
reiting_max=-1000000000000000
film_max= None
reiting_min=10000000000000000
film_min= None

for i in range(films):
    film_name = input()
    reiting = float(input())
    average = average+reiting
    if reiting >= reiting_max:
        reiting_max=reiting
        film_max=film_name
    elif reiting <= reiting_min:
        reiting_min=reiting
        film_min=film_name

average_fin = average/films
print(f"{film_max} is with highest rating: {reiting_max}")
print(f"{film_min} is with lowest rating: {reiting_min}")
print(f"Average rating: {average_fin:.1f}")
