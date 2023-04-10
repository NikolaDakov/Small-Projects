budget = float(input())
season = input()
place = ''
type_h = ''
total = 0
if budget <= 100:
    place = 'Bulgaria'
    if season == 'summer':
        type_h = 'Camp'
        total = budget * 30/100
    elif season == 'winter':
        type_h = 'Hotel'
        total = budget * 70/100
elif budget <= 1000:
    place = 'Balkans'
    if season == 'summer':
        type_h = 'Camp'
        total = budget * 40/100
    elif season == 'winter':
        type_h = 'Hotel'
        total = budget * 80/100
elif budget > 1000:
    place = 'Europe'
    type_h = 'Hotel'
    total = budget * 90/100
print(f'Somewhere in {place}')
print(f'{type_h} - {total:.2f}')
