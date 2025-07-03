player_hp = 10
sword_goblin_hp = 5
bow_goblin_hp = 3
turn = 0
weapons = ["Sword", "Axe", "Bow"]
special_attacks = ["Flame burst", "Ice shards", "Shade strike", "Earth palm"]

chosen_weapon = input("What weapon would you like to equip?" + str(weapons))
if chosen_weapon in weapons:
    print("You equiped " + chosen_weapon)
    chosen_spc = input("What is your special attack?" + str(special_attacks))
    if chosen_spc in special_attacks:
        print("You gain " + chosen_spc + "Now you're ready to battle")
        turn = 1
    else:
        print("You tried to cast a spell you dont know, it backfired, you're dead now :)")
else:
    print("You didnt have a weapon to defend yourself and you died, womp womp")

if turn == 1:
    attacking = input("Two enemies stand before you, would you like to attack sword goblin or bow goblin?")
    if attacking == "bow goblin" and chosen_weapon == "Bow":
        print("You fire at the bow goblin with your bow and hit it with your " + chosen_spc + " which finishes it off")
        bow_goblin_hp = 0
    elif:
    attacking == "bow goblin" and chosen_weapon != "Bow"
