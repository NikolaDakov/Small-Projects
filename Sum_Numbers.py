counter = int(input())
sum_number = 0

while True:
    n = int(input())
    sum_number += n
    if sum_number >= counter:
        print(sum_number)
        break
