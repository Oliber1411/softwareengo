rooms = {
    "entrance": {
        "description": "The delapitated entrance of the soup kitchen, the only way to continue is north. Or you could just leave",
        "exits": {"north": "hallway"},
        "items": []
    },
    "restraunt": {
        "description": "",
        "exits": {"south": "cell", "east": "control_room", "west": "armoury"},
        "items": []
    },
    "armoury": {
        "description": "Stacks of weapons and equipment. There’s a blaster on the shelf.",
        "exits": {"east": "hallway"},
        "items": ["blaster"]
    },
    "control_room": {
        "description": "Screens flash with security alerts. A terminal glows. North leads to the escape pod.",
        "exits": {"west": "hallway", "north": "escape_pod"},
        "items": ["keycard"]
    },
    "escape_pod": {
        "description": "A single escape pod sits waiting. The panel blinks: Insert Keycard.",
        "exits": {"south": "control_room"},
        "items": []
    }
}

starting_room = "entrance"
