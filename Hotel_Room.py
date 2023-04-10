month = input()
day = int(input())
studio = 0
apartment = 0
total1 = 0
total2 = 0
if month == 'May' or month == 'October':
    studio = 50
    total1 = day * studio
    if 14 > day > 7:
        total1 = (day * studio) - ((day * studio) * 5/100)
    elif day > 14:
        total1 = (day * studio) - ((day * studio) * 30 / 100)
    apartment = 65
    total2 = day * apartment
    if day > 14:
        total2 = (day * apartment) - ((day * apartment) * 10 / 100)
elif month == 'June' or month == 'September':
    studio = 75.20
    total1 = day * studio
    if day > 14:
        total1 = (day * studio) - ((day * studio) * 20 / 100)
    apartment = 68.70
    total2 = day * apartment
    if day > 14:
        total2 = (day * apartment) - ((day * apartment) * 10 / 100)
elif month == 'July' or month == 'August':
    studio = 76
    total1 = day * studio
    apartment = 77
    total2 = day * apartment
    if day > 14:
        total2 = (day * apartment) - ((day * apartment) * 10 / 100)
print(f'Apartment: {total2:.2f} lv.')
print(f'Studio: {total1:.2f} lv.')
