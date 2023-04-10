number_location = int(input())
day_avr = 0
for _ in range(number_location):
    target_avr_income = float(input())
    days_dig = int(input())
    for n in range(1, days_dig + 1, 1):
        day_income = float(input())
        day_avr += day_income/days_dig
    if target_avr_income <= day_avr:
        print(f'Good job! Average gold per day: {abs(day_avr):.2f}.')
        day_avr -= day_avr
    elif target_avr_income > day_avr:
        print(f'You need {abs(target_avr_income - day_avr):.2f} gold.')
