type_projection = input()
rows = int(input())
colum = int(input())

Premiere = 12.00
Normal = 7.50
Discount = 5.00
total = 0
if type_projection == 'Premiere':
    total = Premiere * (rows * colum)
elif type_projection == 'Normal':
    total = Normal * (rows * colum)
elif type_projection == 'Discount':
    total = Discount * (rows * colum)
print(f'{total:.2f} leva')
