def show_location(room_name, rooms): # This line defines a function called show_location 
    room = rooms[room_name]
    print("\nYou are in", room_name.upper())
    print(room["description"])
    if room["items"]:
        print("You see:", ", ".join(room["items"]))
    print("Exits:", ", ".join(room["exits"].keys()))

def input():
    return input("what would you like to do?").lower()

def move(current_room,direction,rooms)