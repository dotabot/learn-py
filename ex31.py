print "You have 3 boxes in front of you.  Do you go through door 1,2,3?"

box = raw_input("> ")

if box == "1":
    print "There's a giant snake. What do you do?"
    print "1. catch it."
    print "2. close it."

    box1 = raw_input("> ")

    if box1 == "1":
        print "The snake bites you and you will soon be dead . Dont worry!"
    elif box1 == "2":
        print "smart move! you are saved.  Good job!"
    else:
        print "Well, i guess thats not an option." 

elif box == "2":
    print "There is loads of cash. what would you do ?"
    print "1. give it to the athorities ."
    print "2. Keep it for yourself."
    print "3. close it."

    box2 = raw_input("> ")

    if box2 == "1" or box2 == "3":
        print "You are completely out of your mind!"
    else:
        print "Dont you think thats selfish ?"

else:
    print "i am sorry its an empty box!"