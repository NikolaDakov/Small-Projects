type_flower = input()
num_flower = int(input())
budget = int(input())

price_Roses = 5
price_Dahlias = 3.80
price_Tulips = 2.80
price_Narcissus = 3
price_Gladi = 2.5
total = 0

if type_flower == "Roses":
    if num_flower > 80:
        total = (price_Roses * num_flower) - ((price_Roses * num_flower) * 10/100)
    else:
        total = price_Roses * num_flower
elif type_flower == "Dahlias":
    if num_flower > 90:
        total = (price_Dahlias * num_flower) - ((price_Dahlias * num_flower) * 15/100)
    else:
        total = price_Dahlias * num_flower
elif type_flower == "Tulips":
    if num_flower > 80:
        total = (price_Tulips * num_flower) - ((price_Tulips * num_flower) * 15/100)
    else:
        total = price_Tulips * num_flower
elif type_flower == "Narcissus":
    if num_flower < 120:
        total = (price_Narcissus * num_flower) + ((price_Narcissus * num_flower)  * 15/100)
    else:
        total = price_Narcissus * num_flower
elif type_flower == "Gladiolus":
    if num_flower < 80:
        total = (price_Gladi * num_flower) + ((price_Gladi * num_flower) * 20/100)
    else:
        total = price_Gladi * num_flower

left = budget - total
need = total - budget
if budget >= total:
    print(f'Hey, you have a great garden with {num_flower} {type_flower} and {left:.2f} leva left.')
elif budget < total:
    print(f'Not enough money, you need {need:.2f} leva more.')
