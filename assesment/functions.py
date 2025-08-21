from data import *

def show_location(room_name, rooms): # This line defines a function called show_location 
    room = rooms[room_name]
    print(room_name)
    print(room["description"])
    if room["items"]:
        print("You see:".join(room["items"]))
    print("Exits:".join(room["exits"].keys()))

def movement(current_room,direction,rooms):
    if direction in rooms[current_room]["exits"]:
        return rooms[current_room]["exits"][direction]
    else:
        print("you cant go that way")
        return current_room