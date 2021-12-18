count = int(input())
dishes = input()
detergent = 0
counter = 0
clean_dishes = 0
clean_teng = 0

detergent = count * 750

while dishes != 'End':
    dishess = int(dishes)
    counter += 1

    if counter % 3 == 0 and counter != 0:
        ready_15 = dishess * 15
        detergent -= ready_15
        clean_teng += dishess
        if detergent < 0:
            print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
            break
    else:
        ready_5 = dishess * 5
        detergent -= ready_5
        clean_dishes += dishess
        if detergent < 0:
            print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
            break
    dishes = input()
else:
    print(f"Detergent was enough!")
    print(f"{clean_dishes} dishes and {clean_teng} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")
