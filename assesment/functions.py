from data import *
import time
import os
import sys

def animate(text, delay = 0.04):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def show_location(room_name, rooms):
    room = rooms[room_name]
    animate(room.get("description", ""))
    items = room.get("items", [])
    if items:
        animate("You see: " + " ".join(items))
    exits = room.get("exits", {}).keys()
    if exits:
        animate("Exits: " + " ".join(exits))

def movement(current_room, action, rooms):
    action = (action or "").strip().lower()
    exits = rooms[current_room].get("exits", {})
    if action in exits:
        return exits[action]
    animate("You can't go that way.")
    return current_room

def take_item(current_room, item, rooms, inventory):
    items = rooms[current_room].get("items", [])
    if item in rooms[current_room].get("items", []):
        inventory.append(item), items.remove(item)
    else:
         animate("You found no such thing.")

def ending(current_room, inventory):
    if current_room == "exit":
        if "canned soup" in inventory and "canned meat" in inventory and "canned tomatoes" in inventory:
            animate("")
            animate("") 
        elif "canned soup" in inventory and "canned tomatoes" in inventory or "canned soup" in inventory and "canned_meat" in inventory or "canned_tomatoes" in inventory and "canned_meat" in inventory:
            animate("You manage to uncover")
            animate("")                   
        elif "canned soup" in inventory or "canned tomatoes" in inventory or "canned meat" in inventory:
            animate("You manage to find a single can of food in the soup kitchen before deciding to leave. As you stumble through the snow you stomach begins to rumble. You crack open the food you took from the sopu kitchen and eat, it stifles your hunger for now. As you continue to walk you hear a voice behind you 'HEY YOU!' a man with a gun is behind you 'Theres a tax for walkin around these parts. You got any food on ya? No? Well thats just too bad...' ")
            animate("ENDING: Taxxed")
        else:
            animate("you leave the soup kitchen with no food to your name, deviding that its not worth it. As you stumble through the snow you stomach begins to rumble, begging for food. You collapse on the freezing ground wishing you had found something, anything in that soup kitchen.")
            animate("ENDING: Starved")
            
def scarychase(time):
    if time == 0:
        animate("You feel a presence near you... HIDE!")
    if time == -1:
        animate("Something is breathing down your neck, you have to hide.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')