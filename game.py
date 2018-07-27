print ("""Hello and welcome to my game.
Please note that this game is story based and thereore makes the 
player (you) in conrtol""")
    
Name = raw_input("Please provide your name. ")
    
print ("""You are a traveling gem on homeworld, doing your diamonds biding.
Your diamond (Blue diamond) has requisted your presence. 
You arrive at Blue diamond's paliquien, nervous but confident.""")
    
print ("You: My Diamond")
    
print ("Blue: Ah, %s there you are. I have a special mission for you.")
    
print ("You: Yes, my Diamond?")
    
print ("""Blue: I need you to investigate a distburance in White Diamond's 
paliquien.""")
    
#variables
obey = 0
disobey = 0
run = 0
done = False
A = 1
B = 1
C = 1
D = 1
A = "A"
B = "B"
C = "C"
D = "D"

# Start main loop
while not done:
    shattered = disobey
    freedom = run
    reward = obey
    A = "A"
    B = "B"
    C = "C"
    D = "D" 
    
    print("A. Investigate White Diamond's paliquien.")
    print("B. Disobey and rebel.")
    print("C. Run")
    print("D. Quit")
        
    userInput = input("Your choice? ")
    
        
    # Quit
    if userInput == "D":
        done = True
   
    # Investigate White Diamond's paliquien
    elif userInput == "A":
        print("You sneak onto White Diamond's paliquien only to find her Pearl standing by herself.")
        print("You ask what she is doing. She doesn't respond.")   
        print("You turn to leave, but then White Diamond's pearl speaks.")
        print("Pearl: White Diamond did not requist your precense.")
        print("You: uh...")
        
        #variables
        A = "a"
        B = "b"
        C = "c"
        D = "d"
        
        # Start main loop 
        while not done:
            A = "a"
            B = "b"
            C = "c"
            D = "d"
            
            print("A. Blue diamond told me to investigate here.")
            print("B. What are you doing here?")
            print("C. Nothing.")
            print("D. Just passing by.")
            
            userInput = input("Your choice? ")
            
            # Blue diamond told me to investigate here
            if userInput == "a":
                print("White diamond's pearl looks you up and down, she pauses for a second, then floats over to you.")
                print("For a second she just stands in front of you, then you are absorbed into a small white bubble.")
                print("In a matter of seconds the bubble sinks into the floor, leaving you standing in front of the terrifying White Diamond.")
                print("You see something out of the corner of your eye. Your heart stops")
                print("It's Pink Diamond! After all these years, it's her.")
                print("White Diamond looks down at you.")
                print("White: Who are you?")
                print("You: I-uh......")
                print("White: Well?")
                print("You: Im Pearl, facet 21, c-cut zh.")
                print("White: And what are you doing here?")
                print("You: Blue Diamond requisted that I investigate a disturbance on your paliquin.")
                print("White: Well, you tell Blue that there is nothing wrong with my paliquin.")
                print("You go to turn, but before you can leave White Diamond lifts her arm and shoots a powerful blast that hits you in your left eye.")
                
            
            # What are you doing here
            if userInput == "b":
                print("White's pearl stares you down as you take a step forward.")
                print("WPearl: Im White Diamonds pearl.")
                print("You: Oh")
                print("WPearl: Who are you?")
                print("Without thinking, you run towards White's Pearl.")
                print("White Pearl saw this coming a mile away and, with grace, kicks you back.")
                print("Instead of hitting the wall, you go THROUGH the wall.")
                print("You get up only to find your in a room with White Diamond.")
                print("Before you could completely ajust to your surroundings, White Diamond, Furius that you interupted her, shoots a blast right at your left eye")
                print("You are then transported to a gem prison where you see a Peridot, a Agate, and a Saphire.")
                
            # Nothing
            if userInput == "c":
                print("White's pearl, who is claerly suspicous, whatches you as you walk forward towards the end of the paliquien.")
                print("Pearl: Is there something your looking for?")
                print("You: Yes but I don't know what....")
                print("Your eyes widen as you find the disturbance. You have walked in on a conversation between Pink and White Diamond.")
                print("White Diamond is furius that you interupted her and, acting on this rage, shoots a blast at your left eye.")
                print("White Diamond laughs as she watches you scream in pain.")
                print("Pink Diamond stares at you, terrified.")
                print("White: I know just what to do with you")
            
            # Just passing by
            if userInput == "d":
                print("White's pearl looks at you and then repeats: White Diamond did not requist your presence.")
                print("You take a step foward, and WPearl immediately reacts.")
                print("Before you know it you have a spear through your stomach.")
                print("You are poofed.")
                print("When you form you are in White's room, and she standing right in front of you.")
                print("White: So, you were just.....passing by?")
                print("You: Y-yes.")
                print("White: LIAR!!!!")
                print("White Diamond then fires a blast at you.")
                print("You go to run when the blast hits your left eye.")
                
    # Disobey and rebel
    elif userInput == "B":
        print("You disobey a direct oder from Blue, and she is not happy.")
        print("She poofs you and shatters you on the spot.")
        done = True
            
    # Run
    elif userInput == "C":
        print("Before Blue can react, you run to the nearest ship.")
        print("You make it to the ship and fly to the only free colony: Earth.")
        done = True
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    