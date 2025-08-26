from functions import show_location, movement, take_item, ending, scarychase, clear_screen
from data import rooms, starting_room
from colorama import Fore, Style
import time
import sys
import os
def main():
    inventory = [""]
    current_room = starting_room
    item = ""
    time = 3
    while True:
        scarychase(time)
        show_location(current_room, rooms)
        ending(current_room, inventory)
        time = time -1
        if current_room == "exit":
            break
        action = input("What would you like to do?").strip().lower()
        clear_screen()
        if action in {"quit",}:
            print("Goodbye!")
            break
        if action.startswith("go "):
            action = action[3:].strip()
            current_room = movement(current_room, action, rooms)
        elif action.startswith("take "):
            item = action[5:].strip()
            take_item(current_room, item, rooms, inventory)

        

if __name__ == "__main__":
    main()
