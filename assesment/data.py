from colorama import init, Fore, Style


rooms = {
    "entrance": {
        "description": "The delapitated entrance of the soup kitchen, the only way to continue is north. Or you could just leave",
        "exits": {"north": "dining_room", "south": "exit"},
        "items": []
    },
    "dining_room": {
        "description": "the main dining_room, once filled with life is now abondened, save for one can of soup",
        "exits": {"south": "entrance", "east": "left_security_hall", "west": "ball_pit", "north": "kitchen_hall"},
        "items": ["canned_soup"]
    },
    "left_security_hall": {
        "description": "A dingy hallway, a lone security camera hooked to the wall, you know it has no power but you cant shake the feeling you're being watched",
        "exits": {"east": "security"},
        "items": []
    },
    "ball_pit":{
        "description": "A decayed kids ball pit, the plastic crunches beneath, could serve has a hiding spot",
        "exists": {"east": "dining_room"},
        "items": []
    },
    "kitchen_hall":{
        "description": "You can catch a whiff of the rotten decaying food that must be in the kitchen from here, its disgusting.",
        "exists": {"south": "dining_room", "north" : "kitchen"},
        "items": []
    },
    "security": {
        "description": "Cracked screens line the walls, their darkened displays only reflecting your own decrepit face. A flashlight lay alone on the desk",
        "exits": {"west": "left_security_hall", "north": "right_security_hall"},
        "items": ["flashlight"]
    },
    "right_security_hall": {
        "description": "Dirty papers line the ground of this dingy hall, despite the lack of camera you fell you're being watched.",
        "exits": {"south": "security", "west": "kitchen"},
        "items": []
    },
    "kitchen": {
        "description": "The repugnent smell of rotting food and moldy floors would be enough to make you leave right now if you werent so desperate for food. Luckily for you a single unoppened can sits on bench top",
        "exits": {"south": "storage", "east": "right_security_hall", "west": "employee_loungue"},
        "items": ["canned_food"]
    },
    "storage": {
        "description": "The room is filled from bottom to top with mold, maggots crawl along the rusted metal shelves which once held something that might be considered edible",
        "exits": {"north": "kitchen", "south": "freezer"},
        "items": []
    },
    "freezer": {
        "description": "That awful smell which permiated the storage room dissapates as you enter the chilling tempretures of the freezer, this room would hold wel preservered meat if someone or something hadnt gotten to it first.",
        "exits": {"north": "storage"},
        "items": []
    },
    "employee_loungue": {
        "description": "A room for resting, no time now though, not that you would want to the loungue itself is destroyed. You notice an employee ID sitting on a table top.",
        "exits": {"east": "admin", "north": "bathroom"},
        "items": ["ID"]
    },  
    "admin": {
        "description": "Hm, an admin room for a ressteraunt? odd but insiginificant",
        "exits": {"west": "employee_loungue"},
        "items": []
    }, 
    "bathroom": {
        "description": "An abhorrently disgusting bathroom, even for the standards of an apocolypse this is truly putrid.",
        "exits": {"south": "employee_loungue"},
        "items": []
    },             
}

starting_room = "entrance"
