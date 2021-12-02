month=input().lower()
nights=int(input())

rent_studio=None
rent_apartm=None

if month == 'may' or month == 'october':
    rent_studio = 50 * nights
    rent_apartm = 65 * nights
    if nights > 7 and nights <= 14:
        rent_studio = (50 * nights) - (50 * nights * 0.05)
    elif nights > 14:
        rent_studio = (50 * nights) - (50 * nights * 0.30)
        rent_apartm = (65 * nights) - (65 * nights * 0.10)

elif month == 'june' or month == 'september':
    rent_studio = (75.20 * nights)
    rent_apartm = (68.70 * nights)
    if nights > 14:
        rent_studio = (75.20 * nights) - (75.20 * nights * 0.20)
        rent_apartm = (68.70 * nights) - (68.70 * nights * 0.10)

elif month=='july' or month=='august':
    rent_studio = 76 * nights
    rent_apartm = 77 * nights
    if nights > 14:
        rent_apartm = (77 * nights) - (77 * nights * 0.10)


print(f'Apartment: {rent_apartm:.2f} lv.')
print(f'Studio: {rent_studio:.2f} lv.')