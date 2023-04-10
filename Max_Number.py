import sys
max_number = - sys.maxsize

while True:
    i = input()
    if i == 'Stop':
        break
    if float(i) >= max_number:
        max_number = float(i)


print(f'{max_number:.0f}')
