from sys import exit
def gold_room():
    print("This room is full of gold. How much do you take?")
    choice = input(">")
    if "1" in choice or "0" in choice:
        how_much = int(choice)
    else:
        dead("Man learn to type a number")
    if how_much < 50 :
        print("Good man you are not greedy. You win")
        exit(0)
    else:
        dead("You are a greedy bastard, You die")
        
def bear_room():
    print("There is a bear in the room,\n the bear has honey \n There fat bear is infront of another door \n How are you going to move the bear? \n take honey? \n taunt bear? \n open door")
    bear_moved = False
    while True:
        choice = input(">")
        if choice == "take honey":
            dead("The Bear looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door \n You are free to go in")
            bear_moved = True
        elif choice == "taunt bear " and bear_moved:
            dead("The bear gets angry and chews your legs off")   
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I don't know what this means")
            
def ola_room():
    print("The great evil ola appears in the room, \n He it whatever stares at you and you go insane, \n Do you flee for your life or eat your head?")
    choice = input(">")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty")
    else:
        ola_room()
    
def dead(why):
    print(why,"Good job")
    exit(0)
    
def start():
    print("You are in a dark room with two doors, \n one on your left and one on your right, \n Which one do you take?")
    choice = input(">")
    if choice == "left":
        bear_room()
    elif choice == "right":
        ola_room()
    else:
        dead("You stumble around the room till you die")
start()