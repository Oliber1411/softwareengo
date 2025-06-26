
badthing = input("What did they do? (ignored, insult, apologised, praised) ")
likes = (input("did they like your recent posts? (True / False)(case sensitive))"))
friend = (input("Are they your friend in real life? (True / False)"))

if badthing == "insult" or badthing == "ignored" and friend == "False":
    print("BLOCKED!") 
elif badthing == "insult" or badthing == "ignored" and friend == "True":
    print("Mute")
elif friend == "True":
    print("Follow")
else:
    print("Unfollow")

