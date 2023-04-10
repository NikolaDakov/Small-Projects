import math
number_tournament = int(input())
start_points = int(input())

won = 0
gain = 0

w = 2000
f = 1200
sf = 720

for _ in range(number_tournament):
    finish = input()
    if finish == 'W':
        gain += w
        won += 1
    elif finish == 'F':
        gain += f

    elif finish == 'SF':
        gain += sf


print(f'Final points: {gain + start_points}')
print(f'Average points: {math.floor(gain/number_tournament)}')
print(f'{won/number_tournament * 100:.2f}%')
