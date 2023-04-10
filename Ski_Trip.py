days = int(input())
type_room = input()
review = input()

room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00

days = days - 1
total = 0

if type_room == 'room for one person':
    total = days * room_for_one_person
elif type_room == 'apartment':
    total = days * apartment
elif type_room == 'president apartment':
    total = days * president_apartment

if days < 10:
    if type_room == 'apartment':
        total -= (total * 30 / 100)
    elif type_room == 'president apartment':
        total -= (total * 10 / 100)
elif 10 < days < 15:
    if type_room == 'apartment':
        total -= (total * 35 / 100)
    elif type_room == 'president apartment':
        total -= (total * 15 / 100)
elif days > 15:
    if type_room == 'apartment':
        total -= (total * 50 / 100)
    elif type_room == 'president apartment':
        total -= (total * 20 / 100)
if review == 'positive':
    total += total * 25/100
elif review == 'negative':
    total -= total * 10/100
print(f'{total:.2f}')
