name = input()
avr = 0
n = 0
fail = 0
while True:
    num = float(input())
    if 2.00 <= num <= 6.00:
        n += 1
        avr += num
        if num <= 4.00:
            fail += 1
            if fail > 1:
                break
        elif n == 12:
            break
    else:
        pass


avr = avr / n
if fail > 1:
    print(f'{name} has been excluded at {n - 1 :.0f} grade')
else:
    print(f'{name} graduated. Average grade: {avr:.2f}')
