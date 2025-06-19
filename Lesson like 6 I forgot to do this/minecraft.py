Username = str(input("Whats your user name? ")) 
Blocks =  int(input("How many blocks do you have? "))
Weight = float(input ("How much does a block weigh? "))
Time = input("Is it daytime (yes or no (case sensitive))")

while Blocks < 10:
 Addblocks =+ int (input("How many blocks would you like to add?")) 
 Blocks = Addblocks + Blocks
 Neededblocks = 10 - Blocks
 print("You need more blocks to survive the night, collect atleast " + str(Neededblocks) + " more")

Finalweght = Blocks*Weight

print("Your username is " + Username + " you have " + str(Blocks) + " blocks which weighs " + str(Finalweght))
if Time == "yes":
 print("its day")
else:
 print("its not day, aaahhhhhhhh, there are mobs, youre gonna die no matter what because im too lazy to code like a weapon or something for this glorified text adventure game")


