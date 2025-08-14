from functions import show_location, movement
from data import rooms, starting_room



def main():
    current_room=starting_room

    show_location(current_room,rooms)
    direction = input("Where would you like to go?")
    movement(current_room, direction)


main()