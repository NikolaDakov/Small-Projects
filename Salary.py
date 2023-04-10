tabs = int(input())
salary = float(input())

Facebook = 150
Instagram = 100
Reddit = 50
for _ in range(tabs):
    type_tabs = input()
    if type_tabs == 'Facebook':
        salary -= Facebook
    elif type_tabs == 'Instagram':
        salary -= Instagram
    elif type_tabs == 'Reddit':
        salary -= Reddit
if salary <= 0:
    print(f'You have lost your salary.')
else:
    print(f'{salary:.0f}')
