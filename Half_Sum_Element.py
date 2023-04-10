import sys
n = int(input())
total = 0
diff = 0
max_number = -sys.maxsize
for _ in range(n):
    number = int(input())
    total += number
    if number > max_number:
        max_number = number

if max_number == total - max_number:
    print(f'Yes\nSum = {abs(max_number)}')
else:
    diff = max_number - (total - max_number)
    print(f'No\nDiff = {abs(diff)}')
