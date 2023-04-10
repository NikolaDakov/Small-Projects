count_location = int(input())

for _ in range(count_location):
    expected_gold = float(input())
    count_days_working = int(input())

    mined_gold = 0.0
    for work_day in range(count_days_working):
        worked_gold = float(input())
        mined_gold += worked_gold

    mined_gold = mined_gold / float(count_days_working)
    if mined_gold >= expected_gold:
        print(f'Good job! Average gold per day: {abs(mined_gold):.2f}.')
    else:
        print(f'You need {abs((expected_gold - mined_gold)):.2f} gold.')