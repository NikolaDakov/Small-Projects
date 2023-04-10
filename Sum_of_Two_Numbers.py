start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

counter = 0
condition = False

for num1 in range(start_interval, end_interval + 1):
    for num2 in range(start_interval, end_interval + 1):
        counter += 1
        if num1 + num2 == magic_number:
            condition = True
            print(f'Combination N:{counter} ({num1} + {num2} = {magic_number})')
            break

    if condition:
        break
if not condition:
    print(f'{counter} combinations - neither equals {magic_number}')
