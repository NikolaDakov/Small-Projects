txt = input()

letter1 = 0
letter2 = 0
letter3 = 0
letter4 = 0
letter5 = 0


for b in range(0, len(txt)):

    if txt[b] == 'a':
        letter1 += 1
    elif txt[b] == 'e':
        letter2 += 2
    elif txt[b] == 'i':
        letter3 += 3
    elif txt[b] == 'o':
        letter4 += 4
    elif txt[b] == 'u':
        letter5 += 5
total = letter1 + letter2 + letter3 + letter4 + letter5
print(total)
