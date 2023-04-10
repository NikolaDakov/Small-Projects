groups = int(input())

total = 0
musala = 0
monblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(groups):
    people_per_group = int(input())
    if people_per_group <= 5:
        musala += people_per_group
    elif 6 <= people_per_group <= 12:
        monblanc += people_per_group
    elif 13 <= people_per_group <= 25:
        kilimanjaro += people_per_group
    elif 26 <= people_per_group <= 40:
        k2 += people_per_group
    elif people_per_group >= 41:
        everest += people_per_group

total = musala + monblanc + kilimanjaro + k2 + everest
musala = musala / total * 100
monblanc = monblanc / total * 100
kilimanjaro = kilimanjaro / total * 100
k2 = k2 / total * 100
everest = everest / total * 100


print(f'{musala:.2f}%\n{monblanc:.2f}%\n{kilimanjaro:.2f}%\n{k2:.2f}%\n{everest:.2f}%')
