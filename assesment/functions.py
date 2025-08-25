from data import *

def show_location(room_name, rooms):
    room = rooms[room_name]
    print(room.get("description", ""))
    items = room.get("items", [])
    if items:
        print("You see: " + " ".join(items))
    exits = room.get("exits", {}).keys()
    if exits:
        print("Exits: " + " ".join(exits))

def movement(current_room, action, rooms):
    action = (action or "").strip().lower()
    exits = rooms[current_room].get("exits", {})
    if action in exits:
        return exits[action]
    print("You can't go that way.")
    return current_room

def take_item(current_room, item, rooms, inventory):
    items = rooms[current_room].get("items", [])
    if item in rooms[current_room].get("items", []):
        inventory.append(item), items.remove(item)
    else:
         print("You found no such thing.")

def ending(current_room, inventory):
    if current_room == "exit":
        if "canned_soup" in inventory and "canned_meat" in inventory and "canned_tomatoes" in inventory:
            print("")
            print("") 
        elif "canned_soup" in inventory and "canned_tomatoes" in inventory or "canned_soup" in inventory and "canned_meat" in inventory or "canned_tomatoes" in inventory and "canned_meat" in inventory:
            print("You manage to uncover")
            print("")                   
        elif "canned_soup" in inventory or "canned_tomatoes" in inventory or "canned_meat" in inventory:
            print("You manage to find a single can of food in the soup kitchen before deciding to leave. As you stumble through the snow you stomach begins to rumble. You crack open the food you took from the sopu kitchen and eat, it stifles your hunger for now. As you continue to walk you hear a voice behind you 'HEY YOU!' a man with a gun is behind you 'Theres a tax for walkin around these parts. You got any food on ya? No? Well thats just too bad...' ")
            print("ENDING: Taxxed")
        else:
            print("you leave the soup kitchen with no food to your name, deviding that its not worth it. As you stumble through the snow you stomach begins to rumble, begging for food. You collapse on the freezing ground wishing you had found something, anything in that soup kitchen.")
            print("ENDING: Starved")
            
