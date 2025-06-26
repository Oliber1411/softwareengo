weapons = ["Sword", "Axe", "Bow"]
special_attacks = ["Flame burst", "Ice shards", "Shade strike", "Earth palm"]
choosenweapon = input("Choose weapon:" + str(weapons))

if choosenweapon in weapons: 
    choosenspecial = input("Choose special attack" + str(special_attacks))
    if choosenspecial in special_attacks:
        print("Your weapon is " + str(choosenweapon) + " and your special attack is " + str(choosenspecial))
    else:
        print("You tried to cast a spell you didnt know, not the best idea, now your dead!")
else:
    print("You didnt choose a weapon and you died, womp womp")
