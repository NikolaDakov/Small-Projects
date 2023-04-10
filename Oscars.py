name_actor = input()
point_academy = float(input())
jury_number = int(input())

total = 0

for _ in range(jury_number):
    name_jury = input()
    point_jury = float(input())
    point_academy += (len(name_jury)) * point_jury/2

    if point_academy > 1250.5:
        print(f'Congratulations, {name_actor} got a nominee for leading role with {point_academy:.1f}!')
        break
else:
    print(f'Sorry, {name_actor} you need {abs(point_academy - 1250.5):.1f} more!')
