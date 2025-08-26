
rooms = {
    "entrance": {
        "description": "The delapitated entrance of the soup kitchen, the only way to continue is north. Or you could just leave",
        "exits": {"north": "dining room","south": "exit"},
        "items": []
    },
    "dining room": {
        "description": "the main dining room, once filled with life is now abondened, save for one can of soup",
        "exits" : {"south": "entrance", "east": "left security hall", "west": "ball pit", "north": "kitchen hall"},
        "items": ["canned soup"]
    },
    "left security hall": {
        "description": "A dingy hallway, a lone security camera hooked to the wall, you know it has no power but you cant shake the feeling you're being watched",
        "exits": {"east": "security"},
        "items": []
    },
    "ball pit":{
        "description": "A decayed kids ball pit, the plastic crunches beneath, could serve has a hiding spot",
        "exits": {"east": "dining room"},
        "items": []
    },
    "kitchen hall":{
        "description": "You can catch a whiff of the rotten decaying food that must be in the kitchen from here, its disgusting.",
        "exits": {"south": "dining room", "north" : "kitchen"},
        "items": []
    },
    "security": {
        "description": "Cracked screens line the walls, their darkened displays only reflecting your own decrepit face. A flashlight lay alone on the desk",
        "exits": {"west": "left security hall", "north": "right security hall"},
        "items": ["flashlight"]
    },
    "right security hall": {
        "description": "Dirty papers line the ground of this dingy hall, despite the lack of camera you fell you're being watched.",
        "exits": {"south": "security", "west": "kitchen"},
        "items": []
    },
    "kitchen": {
        "description": "The repugnent smell of rotting food and moldy floors would be enough to make you leave right now if you werent so desperate for food. Luckily for you a single unoppened can sits on bench top",
        "exits": {"south": "kitchen hall", "east": "right security hall", "west": "employee loungue", "north": "storage"},
        "items": ["canned tomatoes"]
    },
    "storage": {
        "description": "The room is filled from bottom to top with mold, maggots crawl along the rusted metal shelves which once held something that might be considered edible",
        "exits": {"south": "kitchen", "north": "freezer"},
        "items": []
    },
    "freezer": {
        "description": "That awful smell which permiated the storage room dissapates as you enter the chilling tempretures of the freezer, this room would hold wel preservered meat if someone or something hadnt gotten to it first.",
        "exits": {"south": "storage"},
        "items": ["canned meat"]
    },
    "employee loungue": {
        "description": "A room for resting, no time now though, not that you would want to the loungue itself is destroyed. You notice an employee ID sitting on a table top.",
        "exits": {"east": "admin", "north": "bathroom"},
        "items": ["ID"]
    },  
    "admin": {
        "description": "Hm, an admin room for a ressteraunt? odd but insiginificant",
        "exits": {"west": "employee loungue"},
        "items": []
    }, 
    "bathroom": {
        "description": "An abhorrently disgusting bathroom, even for the standards of an apocolypse this is truly putrid.",
        "exits": {"south": "employee loungue"},
        "items": []
    },             
    "exit": {
        "description": "",
        "exits": {},
        "items": []
    },
    "Basement": {
        "description": "",
        "exits": {"south": "employee loungue"},
        "items": []        
    },
}

starting_room = "entrance"
