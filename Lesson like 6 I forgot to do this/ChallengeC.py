
badthing = input("What did they do? (ignored, insult, apologised, praised) ")
likes = (input("did they like your recent posts? (True / False)(case sensitive))"))
friend = (input("Are they your friend in real life? (True / False)"))

if (badthing == "insult" or "ignored") and (friend == "False"):
    print("BLOCKED!") 
elif (badthing == "insult" or "ignored") and (friend == "True"):
    print("Mute")
else:
    print("Follow")
