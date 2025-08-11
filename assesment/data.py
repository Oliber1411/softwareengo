rooms = {
    "entrance": {
        "description": "The delapitated entrance of the soup kitchen, the only way to continue is north. Or you could just leave",
        "exits": {"north": "dining room", "south": "exit"},
        "items": []
    },
    "dining room": {
        "description": "the main dining room, once filled with life is now abondened, save for one can of soup",
        "exits": {"south": "entrance", "east": "left_security_hall", "west": "ball_pit", "north": "kitchen_hall"},
        "items": ["Canned soup"]
    },
    "left_security_hall": {
        "description": "A dingy hallway, a lone security camera hooked to the wall, you know it has no power but you cant shake the feeling you're being watched",
        "exits": {"east": "security"},
        "items": ["blaster"]
    },
    "security": {
        "description": "Cracked screens line the walls, their darkened displays only reflecting your own decrepit face.",
        "exits": {"west": "left_security_hall", "north": "right_security_hall"},
        "items": ["keycard"]
    },
    "right_security_hall": {
        "description": "Dirty papers line the ground of this dingy hall, despite the lack of camera you fell you're being watched.",
        "exits": {"south": "security", "west": "kitchen"},
        "items": []
    },
    "kitchen": {
        "description": "The repugnent smell of rotting food and moldy floors would be enough to make you leave right now if you werent so desperate for food. Luckily for you a single unoppened can sits on bench top",
        "exits": {"south": "security", "west": "kitchen"},
        "items": []
    }
}

starting_room = "entrance"
