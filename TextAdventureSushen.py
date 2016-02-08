#QUEST: THE ROAD TO RUBY CITY, PART 1
from random import choice
from random import randint
from turtle import *
import time

al = Turtle()
al.speed("fastest")
canvas1 = Screen()

#functions
def sword ():
    al.left(45)
    al.forward(40)
    al.right(90)
    al.forward(20)
    al.right(90)
    al.forward(40)
    al.right(90)
    al.forward(20)
    al.right(90)
    al.forward(40)
    al.left(90)
    al.forward(20)
    al.right(90)
    al.forward(10)
    al.right(90)
    al.forward(60)
    al.right(90)
    al.forward(10)
    al.right(90)
    al.forward(20)
    al.back(20)
    al.left(90)
    al.back(10)
    al.left(90)
    al.back(20)
    al.left(90)
    al.forward(100) 
    al.left(45)
    al.forward(14.1421356237)
    al.left(90)
    al.forward(14.1421356237)
    al.left(45)
    al.forward(100)
    al.left(90.5)
    al.forward(10)
    al.left(90)
    al.forward(106)

def wizardStar ():
    for i in range(20):
        al.forward(i * 10)
        al.right(144)

def triangle (numLeft, numBottom, numRight):
    for i in [0, 1, 2]:
        al.forward(100)
        al.left(120)
    numMiddle = (numLeft * numRight) - numBottom
    al.left(90)
    al.penup()
    al.forward(43.3013)
    al.pendown()
    al.write(str(numLeft), font=("Arial", 12, "normal"))

    al.penup()
    al.left(180)
    al.forward(63.3013)
    al.left(90)
    al.forward(47)
    al.pendown()
    al.write(str(numBottom), font=("Arial", 12, "normal"))

    al.left(90)
    al.penup()
    al.forward(53.3013)
    al.penup()
    al.pendown()
    al.write(str(numMiddle), font=("Arial", 12, "normal"))

    al.right(180)
    al.forward(33.3013)
    al.left(90)
    al.forward(50)

    al.left(90)
    al.penup()
    al.forward(43.3013)
    al.pendown()
    al.write(str(numRight), font=("Arial", 12, "normal"))

    al.penup()
    al.right(180)
    al.forward(43.3013)
    al.left(90)

def triangleBottom (numLeft, numBottom, numRight):
    for i in [0, 1, 2]:
        al.forward(100)
        al.left(120)
    numMiddle = "?"
    al.left(90)
    al.penup()
    al.forward(43.3013)
    al.pendown()
    al.write(str(numLeft), font=("Arial", 12, "normal"))

    al.penup()
    al.left(180)
    al.forward(63.3013)
    al.left(90)
    al.forward(47)
    al.pendown()
    al.write(str(numBottom), font=("Arial", 12, "normal"))

    al.left(90)
    al.penup()
    al.forward(53.3013)
    al.penup()
    al.pendown()
    al.write(str(numMiddle), font=("Arial", 12, "normal"))

    al.right(180)
    al.forward(33.3013)
    al.left(90)
    al.forward(50)

    al.left(90)
    al.penup()
    al.forward(43.3013)
    al.pendown()
    al.write(str(numRight), font=("Arial", 12, "normal"))

    al.penup()
    al.right(180)
    al.forward(43.3013)
    al.left(90)
    
numAns1 = randint(3, 21)
numAns2 = randint(3, 21)
numAns3 = randint(3, 21)

numLeft1 = randint(3, 21)
numLeft2 = randint(3, 21)
numLeft3 = randint(3, 21)

numRight1 = randint(3, 21)
numRight2 = randint(3, 21)
numRight3 = randint(3, 21)

def wallPuzzle ():
    #Triangle 1
    al.penup()
    al.left(90)
    al.forward(150)
    al.right(90)
    al.forward(50)
    al.pendown()
    triangle(numLeft1, numLeft2, numLeft3)
    al.right(180)
    
    #triangle 2
    al.penup()
    al.forward(300)
    al.pendown()
    al.right(180)
    triangle(numRight1, numRight2, numRight3)
    #triangle 3
    al.penup()
    al.forward(55)
    al.right(90)
    al.forward(100 + 86.6025)
    al.right(90)
    al.forward(50)
    al.right(180)
    al.pendown()
    numMiddle = "?"
    triangleBottom(numAns1, numAns2, numAns3)

chance = randint(1, 20)    
# Images end #

infoName = input("What is thy name, mighty adventurer? ")
infoAge = input("And how old might you be? ")
i = True
while i:
    try:
        infoGender = input("What is thy gender?, male or female? ")
        i = False
    except ValueError:
        print("Enter your age in a number you fool")

infoHealth = 3

print("    ")
print("Adventurer profile:")
print("Name:- " + infoName)
print("Age:- " + infoAge)
print("Gender:- " + infoGender)

infoAge = int(infoAge)

time.sleep(2)


#Code that decides gender to use in story.
if infoGender == "male":
    infoGender = "his"
else:
    infoGender = "her"

print("    ")

#A different slightly story for different age groups.
if infoAge >= 0 and infoAge <= 21:
    print("the mighty, young adventurer known as " + infoName +
          " whose name echoed all across the relm was getting ready for "
          + infoGender + " quest")
elif infoAge > 21 and infoAge <= 40:
    print("the mighty, well abled adventurer known as " + infoName +
          " whose name echoed all across the relm was getting ready for "
          + infoGender + " quest")
elif infoAge > 40:
    print("the wise adventurer known as " + infoName +
          " whose name echoed all across the relm was getting ready for "
          + infoGender + " quest")

print("    ")

time.sleep(2)

#Selects the class of the character.
classSelect = input("Are you a warrior or a wizard? ")

if classSelect.lower() == "wizard":
    classSelect = "wizard"
    print("ahh a wizard, a wise choice " + infoName +
          ", you are known for various arcane spells and magic, definitely a force to be reckoned with.")
    infoHealth = 3
    time.sleep(2)
    print("As you have chosen to become the wizard you have 3 HP (health points)")
    wizardStar()

    time.sleep(2)
    print("")

        #attributes
    strength = 14
    dexterity = 7
    intelligence = 9
    magic = 5
    time.sleep(2)
    print("Your attributes are: (the lower the better)")
    print("strength - " + str(strength))
    print("intelligence - " + str(intelligence))
    print("dexterity - " + str(dexterity))
    print("magic - " + str(magic))
    

else : #warrior
    classSelect = "warrior"
    print("The ferocious warrior, you are a massive brute who uses "+ infoGender + " sheer power and muscles to destroy his way through enemies with "+ infoGender + " trusty sword")
    infoHealth = 5
    time.sleep(2)
    print("As you have chosen to become the warrior you have 5 HP (health points)")
    sword()

    time.sleep(2)
    print("")

    #attributes
    strength = 9
    dexterity = 7
    intelligence = 10
    magic = 19
    time.sleep(2)
    print("Your attributes are: (the lower the better)")
    print("strength - " + str(strength))
    print("intelligence - " + str(intelligence))
    print("dexterity - " + str(dexterity))
    print("magic - " + str(magic))

time.sleep(3)
    
al.clear()
al.penup()
al.setx(0)
al.sety(0)
al.setheading(0)

print("")
time.sleep(4)
chance = randint(1, 20)
print("\'There will be chance events which basically imitate a dice roll, in these events you have to roll a number higher than your specified attribute to successfully perform that action\'")
time.sleep(8)
print("   ")
print("   ")

print("STORY START: ")
time.sleep(2)
#inventory
print("The sun is just rising above the horizon, you are getting ready for your adventure.")
time.sleep(4)
print("   ")
print("You look around your humble shack and notice a few things you can bring with you, you can carry a maximum of 2 items")
time.sleep(4)

print("   ")
i = True
while i
    inventory1 = input("what\'s the first item you'd like to bring along? :- water, firesticks (matches), oil or a dice. ")
    if "water" or "firesticks" or "matches" or "oil" or "dice" in inventory1.lower:
        print("")
        i = False
    else:
        print("That item is not in your house! Try again")
print("   ")
inventory2 = input("what\'s the second item you'd like to bring along? :- water, firesticks (matches), oil or a dice. ") #How to subtract strings
i = True
while i
    inventory1 = input("what\'s the first item you'd like to bring along? :- water, firesticks (matches), oil or a dice. ")
    if "water" or "firesticks" or "oil" or "matches" or "dice" in inventory2.lower:
        print("")
        i = False
    else:
        print("That item is not in your house! Try again")

inventory = [inventory1, inventory2]
print("You gladly take both the "+ inventory1 + " and the "+ inventory2)
time.sleep(2)
print("   ")

#start#
print("As you step outside your shack a black raven drops a rather odd looking scroll at your feet... ")

time.sleep(2)
print("")

scrollPickup = input("Do you want to pick up the scroll? yes or no ")
scroolPickup = scrollPickup.lower()

if scrollPickup == "yes" in scrollPickup or "y" in scrollPickup:
    print(" ")
    print("You pick up the scroll and open it, a weird glittering substance bursts out of the paper,")
    print("you ignore this \'glitter\' and proceed to read the scroll")
    print("")
    print("\" To the ruby city you must go \"")
    print("\" your own tales you can sew \"")
    print("\" Find the gem that glistens so bright \"")
    print("\" You could be searching day and night \"")
    time.sleep(8)
else:
    print("You walk past the scroll and start walking forward, ")
    print("you begin to realise that perhaps that scroll was your quest")
    print("Guess you should have picked that up huh?")
    print("   ")
    print("END OF STORY!!!")
    exit() # END 1 #

print("  ")
print("Still unsure of what to do, you decide to walk towards the ruby city as that is your only lead")
print("  ")
print("  ")
time.sleep(2)
print("A few miles down the road you notice a rather odd looking troll blocking the path")
time.sleep(2)
print("He seems to be inspecting a horse wagon!")

time.sleep(2)
print("")

#TROLL#
trollApproach = input("Do you approach the troll? yes or no(try to sneak past) ")

if trollApproach == "yes" in trollApproach or "y" in trollApproach:
    print("You walk towards the troll being very cautious.")
    print("")
    time.sleep(1)
    print("\"Hello there\" you exclaim")
    print("")
    time.sleep(1.5)
    print("The troll turns around and looks at you menacingly, you can see the red of his eyes from where you stand")
    time.sleep(2)
    print("It rips off a piece of a nearby tree and starts running at you!")
    time.sleep(2)
    print("")
    print("That didn't go quite as planned did it?")

    if classSelect == "warrior": # trollApproach and warrior
        print("You draw your mighty sword and shield and charge towards the troll.")
        time.sleep(2)
        print("STRENGTH CHANCE EVENT: ")
        time.sleep(2)
        print("you roll: " + str(chance))
        print("")
        if chance < 9: #failed attack troll
            print("You try to swing at the beast ferociously, but you are too slow to react and the troll smashes right into you!")
            infoHealth = infoHealth - 1
            print("")
            time.sleep(2.5)
            print("You lose 1 HP")
            time.sleep(2)
            print("")
            print("It then runs away into the forest before you get up")
        else: # success attack troll
            print("Using your raw physical prowess you accurately stab the troll square in its heart.")
            time.sleep(2.5)
            print("The troll goes down like a house of cards.")
    else: # trollApproach and wizard
        print("You draw your wand and poise for a mystical spell.")
        time.sleep(2.5)
        print("")
        time.sleep(2.5)
        print("MAGIC CHANCE EVENT:")
        time.sleep(2.5)
        print("you roll: " + str(chance))
        if chance < 5: # failed attack troll
            print("your wand sputters with mere sparks instead of electricity and is unable to damage the troll")
            infoHealth = infoHealth - 1
            time.sleep(2.5)
            print("")
            print("The troll smashes into you and runs away before you can get up.")
            time.sleep(2.5)
            print("You lose 1 HP")
        else: # succes attack troll
            print("You gather all the energy you can and hit the troll with all you got")
            time.sleep(2.5)
            print("")
            print("It vanishes into thin air!")

    time.sleep(5)
    chance = randint(1, 20)
    print("")
    print("You walk toward the horse wagon to inspect it.")
    time.sleep(3)
    print("")
    print("It appears to be a royal wagon")
    time.sleep(3)
    print("Inside you find another mysterious note: ")
    print("")
    time.sleep(3)
    print("\"Dear Barbara")
    print("You must not lose this key, it is vital to finding the treasure")
    print("Do not lose it\"")
    time.sleep(3)
    print("")
    print("you look around and almost immediatly find this \"key\"")
    print("")
    print("although it does not look like a key, rather it looks like a weird prism like object")
    print("you decide to keep the key in case you need it")
    print(" ")
    inventory.append("mysteriousKey")
    time.sleep(2)
    print("Inventory:")
    i = 0
    while i < len(inventory):
        print(inventory[i])
        i = i + 1
    time.sleep(3)
                       
else: #if no
    if classSelect == "wizard":
        print("MAGIC CHANCE EVENT:")
        time.sleep(2)
        print("")
        print("you roll: " + str(chance))
        time.sleep(2)
        if chance < 5:
            print("You try to conjur up an invisibility spell but are unsuccessful")
            time.sleep(2)
            print("")
            print("The troll easily detects you and grabs a nearby tree and smashes you with it!")
            infoHealth = infoHealth - 1
            time.sleep(2)
            print("")
            print("you lose 1 HP")
        else:
            print("Using your arcane magic, you quickly conjure up an invisibility shield which makes you near invisible to the naked eye.")
            time.sleep(1)
            print("you easily manage to sneak past the troll.")
            print("  ")
            print("Lucky you learnt that spell a just few weeks ago")
        
    else:
        print("Your heavy metal armour makes a ridiculous clanking noise as you try to sneak past")
        time.sleep(0.5)
        print("The troll is startled when it hears this noise, it takes this as an act of hostility and immediatly procedes to smash you with the wagon.")
        print("  ")
        time.sleep(0.5)
        print("You are completely taken by surprise you get squashed")
        print("Suddenly a mysterious wall appears in front of you ")
        time.sleep(0.5)
        print("Why the hell would you walk past a troll?!!??! You're a goddamn warrior!")
        print("   ")
        time.sleep(0.5)
        print("END OF STORY!!!!")
        exit() # END 2 #

time.sleep(2)
print("")
print("You continue down the path towards the city.")
time.sleep(2)
print("") #The wall
print("As you walk down the path you realise the road is getting narrower every step you take")
time.sleep(2)
print("")
print("The air seemed to get colder and a slight fog became present")
time.sleep(2)
print("")
print("Suddenly a massive wall appeared in front of you! It seemed to have just fell from the sky!!!!")
time.sleep(2)
print("The wall had some sort of weird inscriptions on it, it was some sort of puzzle!")
time.sleep(2)
print("")

print("INTELLIGENCE CHANCE EVENT: (to see if you can attempt this puzzle)")
print("you roll: " + str(chance))
if chance < 3: #Failed wall attempt
    print("You try and distinguish the symbols on the wall but u just can't make sense of them")
    time.sleep(2)
    print("")
    print("I guess you are stuck here huh?")
    time.sleep(2)
    print("")
    print("Tough luck mate....")
    print("END OF STORY!!!!")
    exit()
    #END 3 #
else: #success wall attempt
    print("You gather all the foregin langue and symbols and convert it into simple commonspeak")
    time.sleep(2)
    print("")


    print("You end up with a sketch of the final puzzle")
    time.sleep(2)
    wallPuzzle()
    i = 1

    while i != 0:
        puzzleAnswer = input("What is your answer? (number) ")
        puzzleAnswer = int(puzzleAnswer)
        if puzzleAnswer == numAns1 * numAns3 - numAns2:
            time.sleep(2)
            print("")
            print("The wall spllits open!, the fog clears out the weather get warmer and the path widens")
            time.sleep(2)
            print("")
            print("You gladly continue along the path")
            i = 0
        else:
            time.sleep(2)
            print("")
            print("You type in the number but to no avail, the wall doesn't budge")
            print("try again")
        
time.sleep(2)
chance = randint(1, 20)

#The realisation
print("The glittering substance that got on you when you opened the letter started to glow as you walked past whre the wall once stood")
print("INTELLIGENCE CHANCE EVENT: ")
print("You roll: " + chance)
if classSelect == "warrior":
    if chance < 10:
        print("Hmmm it must be reacting to the weather, you think")
        time.sleep(3)
        print("Wait you fool, its a bloody tracking device")
        print("Honestly how dumb can you be?")
        time.sleep(3)
        print("Reacting to the weather, my narrating arse it is, pfft")
    else:
        time.sleep(2)
        print("The glitter must be some sort of magial tracking device!")
        time.sleep(2)
        print("But why would the same people that provided you with your quest try to hunt you down?")
        i = 5
        while i == 0:
            trapQuestion = input("")
            if "trap" in trapQuestion or "set up" in trapQuestion or "trick" in trapQuestion:
                print("You're right it must be a trap!")
                time.sleep(2)
                print("But who would try to set you up?")
                i = 0
            else:
                print("I don't think that's it, try again")
                i = i - 1
                if i == 0:
                    print("Alright I give up you're too dumb to get this")
                    time.sleep(2)
                    print("Its a trap you fool, someone is trying to set you up")
        

else:
    if chance < 9:
        print("Hmmm it must be reacting to the weather, you think")
        time.sleep(3)
        print("Wait you fool, its a bloody tracking device")
        print("Honestly how dumb can you be?")
        time.sleep(5)
        print("Reacting to the weather, my narrating arse it is, pfft")
    else:
        print("The glitter must be some sort of magical tracking device!")
        time.sleep(2)
        print("But why would the same people that provided you with your quest try to hunt you down?")
        i = 5
        while i == 0:
            trapQuestion = input("")
            if "trap" in trapQuestion or "set up" in trapQuestion or "trick" in trapQuestion:
                print("You're right it must be a trap!")
                time.sleep(2)
                print("But who would try to set you up?")
                i = 0
            else:
                print("I don't think that's it, try again")
                i = i - 1
                if i == 0:
                    print("Alright I give up you're too dumb to get this")
                    time.sleep(2)
                    print("Its a trap you fool, someone is trying to set you up")

time.sleep(5)
print("As you continue along the road, you think deep and hard how you should proceed next")
time.sleep(2)
print("")
print("Some time later you arrive at a rather dreary old sign")
time.sleep(2)
print("It read")
al.clear()
al.penup()
al.setx(-140)
al.sety(0)
al.setheading(0)
al.pendown()
al.write("LEOTON TOWN -->", font=("Candara", 40, "normal"))
time.sleep(3)
print("")
print("You look to the right and see a diverting path and indeed you see a fairly large town")
time.sleep(3)
print("Since the sun was setting and dusk was approaching, you decide to spend the night in Leoton")
time.sleep(2)
print("")
print("As the night fell you visit the local inn to seek shelter")

time.sleep(2)
print("")
print("You are met by a rather shady looking inn keeper, an green ogre with a massive scar across his left eye")
time.sleep(2)
print("\"Nice to see you old friend,\" he says")
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("Leo?")
time.sleep(2)
print("\"How have you been my friend?\"")
time.sleep(2)
print("\"But... But...\"")
time.sleep(3)
print("\"Yes mate, I'm alive and kickin, \"")
print("You thought I was dead didn't ya?\" He cheered patting you on the back")
time.sleep(3)
print("")
print("")


