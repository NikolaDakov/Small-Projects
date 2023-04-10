pastry_type = input()
number_pastry = int(input())
date = int(input())
total = 0
if date <= 15:
    if pastry_type == 'Cake':
        total = number_pastry * 24
    elif pastry_type == 'Souffle':
        total = number_pastry * 6.66
    elif pastry_type == 'Baklava':
        total = number_pastry * 12.60
elif date > 15:
    if pastry_type == 'Cake':
        total = number_pastry * 28.70
    elif pastry_type == 'Souffle':
        total = number_pastry * 9.80
    elif pastry_type == 'Baklava':
        total = number_pastry * 16.98

if date <= 22:
    if 100 <= total <= 200:
        total = total - (15/100 * total)
    elif total > 200:
        total = total - (25/100 * total)
if date <= 15:
    total = total - (10/100 * total)

print(f'{total:.2f}')
