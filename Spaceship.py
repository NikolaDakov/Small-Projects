with_ship = float(input())
long_ship = float(input())
high_ship = float(input())
high_astronaut = float(input())

room_with = 2
room_long = 2
room_high = 0.4
volume = with_ship * long_ship * high_ship
volume_room = (high_astronaut + room_high) * room_long * room_with
people = volume//volume_room
if 3 <= people <= 10:
    print(f'The spacecraft holds {people:.0f} astronauts.')
elif people < 3:
    print(f'The spacecraft is too small.')
elif people > 10:
    print(f'The spacecraft is too big.')
