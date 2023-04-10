budget = int(input())
season = input()
number = int(input())

discount = 0
rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer':
    rent = 4200
elif season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if number <= 6:
    discount = rent * 10 / 100
elif 7 <= number <= 11:
    discount = rent * 15 / 100
elif number > 12:
    discount = rent * 25 / 100
total = rent - discount
if number % 2 == 0:
    extra = total - ((rent - discount) * 5 / 100)
    if budget >= total:
        money = budget - total
        print(f'Yes! You have {money:.2f} leva left.')
    else:
        money = total - budget
        print(f'Not enough money! You need {money:.2f} leva.')
else:
    if budget >= total:
        money = budget - total
        print(f'Yes! You have {money:.2f} leva left.')
    else:
        money = total - budget
        print(f'Not enough money! You need {money:.2f} leva.')
