price_toy = 5
price_sweaters = 15
adult = 0
kids = 0
total_toys = 0
total_sweaters = 0
while True:
    age = input()
    if age == 'Christmas':
        break
    elif float(age) <= 16:
        kids += 1
        total_toys += price_toy
    elif 16 < float(age):
        adult += 1
        total_sweaters += price_sweaters

print(f'Number of adults: {adult}')
print(f'Number of kids: {kids}')
print(f'Money for toys: {total_toys}')
print(f'Money for sweaters: {total_sweaters}')
