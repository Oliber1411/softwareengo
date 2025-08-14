def show_location(room_name, rooms): # This line defines a function called show_location 
    room = rooms[room_name]
    print("\nYou are in", room_name.upper())
    print(room["description"])
    if room["items"]:
        print("You see:", ", ".join(room["items"]))
    print("Exits:", ", ".join(room["exits"].keys()))

def movement(current_room,direction,moved_room):
    if direction in moved_room [current_room] ["exits"]:
        return moved_room, [current_room] , ["exits"] , [direction]
    else:
        print("you cant go that way")
        return current_room