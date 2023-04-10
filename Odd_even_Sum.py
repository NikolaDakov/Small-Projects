number_of_lines = int(input())
even = 0
odd = 0
for i in range(1, number_of_lines + 1):
    current_num = int(input())
    if i % 2 == 0:
        even += current_num
    else:
        odd += current_num

if even == odd:
    print(f'Yes\nSum = {even}')
else:
    diff = abs(even - odd)
    print(f'No\nDiff = {diff}')
