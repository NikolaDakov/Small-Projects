city = input()
sales = float(input())

if city == 'Sofia':
    if 0 <= sales <= 500:
        commission = sales * 5/100
    elif 500 < sales <= 1000:
        commission = sales * 7/100
    elif 1000 < sales <= 10000:
        commission = sales * 8 / 100
    elif sales > 10000:
        commission = sales * 12 / 100
        print(f'{commission:.2f}')
    else:
        print('error')
elif city == 'Varna':
    if 0 <= sales <= 500:
        commission = sales * 4.5 / 100
    elif 500 < sales <= 1000:
        commission = sales * 7.5 / 100
    elif 1000 < sales <= 10000:
        commission = sales * 10 / 100
    elif sales > 10000:
        commission = sales * 13 / 100
        print(f'{commission:.2f}')
    else:
        print('error')

elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        commission = sales * 5.5 / 100
    elif 500 < sales <= 1000:
        commission = sales * 8 / 100
    elif 1000 < sales <= 10000:
        commission = sales * 12 / 100
    elif sales > 10000:
        commission = sales * 14.5 / 100
        print(f'{commission:.2f}')
    else:
        print('error')


else:
    print('error')
