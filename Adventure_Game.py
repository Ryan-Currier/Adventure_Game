#Date: 11/3/25 Author: Ryan Currier
#paste this to run -> & "C:/Users/Ryan/AppData/Local/Python/pythoncore-3.14-64/python.exe" "c:/Users/Ryan/Desktop/Personal Projects/Adventure_Game.py"

import random


class Classes():
    #basically creats the initial dictionary
    def __init__(self):
        self.stats = {}

    #Wizard dictionary - function is filling the stats dict with stat , value
    def wizard_stats(self):
        self.stats = {
            "HP" : 80, 
            "Moves" :{ 
            "Fireball" : 30, 
            "Magic Missle" : 20}
            }

        

    #Barbarian dictionary
    def barbarian_stats(self):
        self.stats = {
            "HP" : 110,
            "Moves" : {
            "Chop" : 15,
            "berserk" : 25}
        }

    #Rogue dictionary
    def rogue_stats(self):
        self.stats = {
            "HP" : 90,
            "Moves" : {
            "Back Stab" : 15,
            "Flash Step" : 25,}
        }



def Battle (player, enemy):
    print("Prepare to Battle!")
    
    #while loop for simple turn based combat
    while player.stats["HP"] > 0 and enemy.stats["HP"] > 0:
            print(f"You're HP: {player.stats['HP']} | Enemy HP: {enemy.stats['HP']}")
            print("Pick your move! ")

            #show your moves
            for move in player.stats["Moves"]:
                print(f" - {move} ({player.stats["Moves"][move]} DMG)")
                
            #input your move
            move_choice = input("Choose your move:".title())

            #Make sure players input is a real & valid move
            if move_choice not in player.stats["Moves"]:
                print("Not Valid Move...    you lost your turn")
                continue # continues on without doing turn
            else:
                #create a dmg value using the move_choice to assign the number
                dmg = player.stats["Moves"][move_choice]
                enemy.stats["HP"] -= dmg
                print(f"You used {move_choice} and dealt {dmg} DMG!!!")
                    
            #create if statement to check if enemy died and break out of loop
            if enemy.stats["HP"] <= 0:
                print("You defeated the enemy!")
                break

            # set the enemy stats into a usuable and readable variable
            enemy_DMG = enemy.stats["ATK"]

            #For Random Crits
            #initally I tried
            # Crit_chance = enemy.stats["CRIT"] --> if Crit_chance == 3: 
            #This does not make it random because the randint in the enemy.stats will be a set number and now randomly rolled every attack so if it is the number it will either always crit or never crit

            Crit_chance = random.randint(1,3)
            if Crit_chance == enemy.stats["CRIT"]:
                enemy_DMG *= enemy.stats["CRITDMG"]
                player.stats["HP"] -= enemy_DMG
                print(f"The enemy hit a critical strike for {enemy_DMG}!!!")
            else:
                player.stats["HP"] -= enemy_DMG
                print(f"The enemy hit you for {enemy_DMG}")

            #check if player is dead
            if player.stats["HP"] <= 0:
                print("You died :(")
                break
                 

#This class allows for easy reusable and organized
# Example -> bandit = Enemy("Bandit", 60, {"Slash": 10, "Throw Dagger": 8}, 3, 2)    
class Enemy: 
    def __init__(self,NAME,HP,ATK,CRIT,CRITDMG):
        self.name = NAME
        self.stats = {
            "HP" : HP,
            "ATK" : ATK,
            "CRIT" : CRIT,
            "CRITDMG" : CRITDMG
        }




#while True:
    #this is the beggining of the game and where the user chooses their path/adventure.
    
print("Welcome to Runeterra!")
User_class = input("""Please choose a class!
                   1. Warrior
                   2. Rogue
                   3. Wizard
                   """).lower()

#Player Object
player = Classes()

#Assigning the class chosen by the user
if User_class == "warrior":
    player.barbarian_stats()
    print("You are a Warrior!")
    #continue
elif User_class == "rogue":
    player.rogue_stats()
    print("You are a Rogue")
    #continue
elif User_class == "wizard":
    player.wizard_stats()
    print("You are a Wizard!")
    #continue
else:
    print("That was not a valid option please type either Warrior, Rogue, or Wizard.")

print("\n Your Stats:")
#.items() means its going to print both values
for stat , value in player.stats.items():
    print(f"{stat} : {value}")
            

Adv_choice = input(str("\nYou have 2 paths - Castle or Forest ").lower())


#Cave Adventure & All Choices

if Adv_choice == "castle":
    print("you enter the Castle!")
    print("""You enter a dark room!
          You interact with an object: bookshelf - chest""")
    room_choice = input(str("\nWhat would you like to interact with? ").lower())
    if room_choice == "bookshelf":
        print("\nyou try to pick up a book, but the bookshelf falls and crushes you")
        #so they can exit the while loop
        Quit = input(str("""\nYOU DIED :(
              press Q to Quit - """).lower())
        
        if Quit == "q":
            print("")
            # break
    elif room_choice == "chest":
        trap_choice = input(str(""" you obtained a gold key!
                                But when you stashed the key a trapdoor opened under you
                                you wake up in a pool of water you can go down 2 paths
                                stairs
                                pool
                                """).lower())
        if trap_choice == "pool":
            print("you enter the pool and get killed by a merrow")

            #so they can exit the while loop
            Quit = input(str("""YOU DIED :(
              press Q to Quit""").lower())
        
            if Quit == "q":
                print("")
                # break
        elif trap_choice == "stairs":
            print ("""you have reached a big door with a small golden lock. You enter your own gold key the door swings open into a big room lit by blue flames
                   you have to fight a merrow to escape alive!""")
            
            #Creating the merrow enemy
            merrow = Enemy("Merrow", 25, 15, 3, 2)
            #Fighting the enemy
            Battle(player, merrow)

            #if player["HP"] < 0:
                #break
            #else:
                #continue
            print ("""You step into the middle of the room and are teleported to a higher plane
                   
                   The Final Boss fight will now commence...""")
            god = Enemy("God", 60, 20, 3, 2)
            Battle(player, god)

            #if player["HP"] < 0:
                #break
            #else:
                #continue

# Forest adventure and choices
if Adv_choice == "forest":
    print("You have entered the Forest!")
    
    path_Choice = input("you have 2 paths you can go down: Darkness - Flowers")

    if path_Choice == "darkness":
        print("You walk down the path and are attack by a Troll")
        
        #Create & Battle Troll enemy
        Troll = Enemy("Troll", 25, 10, 3, 2)
        Battle(player, Troll)


        #This will just exit the player from the game if he loses all hp...
        # -- Not sure if this is necassary or if the battle function has it built in
        #if player["HP"] < 0:
        #    break
        #else:
        #    continue
        
        