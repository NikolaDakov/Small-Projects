n = int(input())
m = int(input())
s = int(input())

for child in range(m, n-1, -1):
    if child == s and child % 2 == 0 and child % 3 == 0:
        break
    elif child % 2 == 0 and child % 3 == 0:
        print(child, end=' ')
