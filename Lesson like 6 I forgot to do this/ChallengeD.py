weapons = ["Sword", "Axe", "Bow"]
special_attacks = ["Flame burst", "Ice shards", "Shade strike", "Earth palm"]
enemies = []
enemies.append("Bow goblin")
enemies.append("Sword goblin")
enemies.append("Fire elementals")
bow_distance = 10
bow_hp = 3
sword_distance = 3
sword_hp = 5
element_distance = 5
element_hp = 6
bow_damage = 1
swordnaxe_damage = 2
special_damage = 2
while element_hp > 0 or sword_hp > 0 or bow_hp > 0:
    
    attacking = input("Choose an enemy to attack" + str(enemies))
    if attacking in enemies:
        choosenweapon = input("Choose weapon to attack with:" + str(weapons))

        if choosenweapon in weapons: 
            choosenspecial = input("Choose special attack" + str(special_attacks))
            if choosenspecial in special_attacks:
                print("You attack " + (attacking) + " using a " + (choosenweapon) + " and your special attack " + (choosenspecial))
                if attacking == "Bow goblin" and choosenweapon == "Bow":
                    print("You attack the bow goblin dealing " + str(bow_damage + special_damage) + " damage" )
                    bow_hp == bow_hp - (bow_damage + special_damage)
                    if bow_hp >= 0:
                        enemies.remove("Bow goblin")
                else:
                    print("Your " + choosenweapon + " is too short and cant get the bow goblin, however your " + choosenspecial + "can and it does" + str(special_damage))
                    bow_hp == bow_hp - special_damage        
            else:
                print("You tried to cast a spell you didnt know, not the best idea, now your dead!")
        else:
            print("You didnt choose a weapon and you died, womp womp")
    else:
        print("You didnt attack an enemy and died, sucks to be you")


