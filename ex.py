# въвеждаме броя на етажите и броя на стаите на един етаж
num_floors = int(input())
num_rooms = int(input())

# обхождаме етажите в обратен ред (от последния към първия)
for floor in range(num_floors, 0, -1):
    # обхождаме стаите на текущия етаж
    for room in range(num_rooms):
        # проверяваме дали текущият етаж е четен или нечетен
        if floor % 2 == 0:
            # изписваме номера на офиса
            print("O{}{}".format(floor, room))
        else:
            # изписваме номера на апартамента
            if room == num_rooms - 1:
                print("L{}{}".format(floor, room))
            else:
                print("A{}{}".format(floor, room))
