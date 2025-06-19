# I should comment my code so I can understand stuff
health = 100
food = 100

lengthincave = input("How long have you spent in the cave?")

health = health - int(lengthincave) * 5

food = food - int(lengthincave) * 3 

print("You now have " + str(health) + " health")
print("You now have" + str(food) + " food left")

if int(health) or int(food) >= 50 :
    print("you are weak")
if int(lengthincave) <= 5 :
    print("You left too early and got attacked") 
else :
    print("Yayyy! you survived!")