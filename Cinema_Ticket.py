day_week = input()

price = 0
if day_week == 'Monday':
    price = 12
elif day_week == 'Tuesday':
    price = 12
elif day_week == 'Wednesday':
    price = 14
elif day_week == 'Thursday':
    price = 14
elif day_week == 'Friday':
    price = 12
elif day_week == 'Saturday':
    price = 16
elif day_week == 'Sunday':
    price = 16

print(price)
