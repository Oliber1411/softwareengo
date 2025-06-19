name = input("What's your name?")

age = input("What is your age?")

Time = input("How long would you like to play? (minutes)")

Snack = input("What snack would you like to bring?")



print("Hello" + name + "You are" + age + "Years old and ready to play in blueys back yard! you'll play for" + Time + "and bring your favourite snack:" + Snack )

games_list = ["Keepy Uppy", "Magic Asparagus", "Shadowlands", "Obstacle Course", "Muffin Cone"]
print(games_list)

print("First game:", games_list[0])
print("Last game:", games_list[-1])

New_game = input("Would you like to add a game?")

games_list.append(New_game)
print(games_list)

games_list[1] = "Magic Wand"
print(games_list)

for game in games_list:
    print("Lets play", game)


def count_games():
    print("Total games:", len(games_list))

count_games()