import random
import time

# LISTS

roam = ["Goblin", "Loot", "Nothing"]
fleeing = ["failed", "fleed"]
battle_luck = ["successful", "missed"]

# INTRO

print("-----------------------------")
print("YOU HAVE ENTERED THE DUNGEONS")
print("-----------------------------")

# FUNCTIONS

def Player():
   return {"health" : 100,
    "coins" : 0,
    "attack" : 15}

def Goblin():
   return {"health" : 60,
    "attack" : 20}

def Bag():
   return{"Potions" : 0}

player = Player()
bag = Bag()

running = True

while running:

# COMMANDS

    print("You Have 3 Options:")
    commands = input("1. Roam\n2. Check Bag\n3. Escape\n4. Merchant\n")

# INVALID COMMAND

    if commands not in  ["1", "2", "3", "4"]:
       print("Invalid Command")
       continue

# MERCHANT

    elif commands == "4":
        print("You decided to check the merchant")
        time.sleep(0.5)
        print("The merchant is selling Health Potions for 30 coins each\nHealth Potion: 30 coins")
        shop = input("Would you like to buy any?\n1. Yes\n2. No")
        
        if shop == "2":
            continue

        if shop == "1":
            amount = input("How many would you like to buy?\n")

            if not amount.isdigit():
                print("Enter Valid Amount")
                continue

            cost = int(amount) * 30
            
            if player["coins"] >= cost:
                player["coins"] -= int(amount) * 30
                bag["Potions"] += int(amount)
                print(f"You have successfully purchased {amount} Potions")
                print("Thank You For Bussiness")
                continue
            
            else:
                print("Not Enough Coins")
                continue

# ESCAPING

    elif commands == "3":
       
        print("You decided to escape from dungeon")
        time.sleep(0.5)
        print("Escaping...")
        time.sleep(1)
        print("You successfully escaped!")
        time.sleep(0.5)

# AGAIN ENTRY

        enter_again = input("Would You Like to Enter Again:\n1: Yes\n2. No\n")

        if enter_again == "1":
            print("You decided to enter Dungeons again")
            time.sleep(0.8)
            continue

        elif enter_again == "2":
            running = False

# CHECK BAG

    elif commands == "2":
       print(f"You have {bag['Potions']} Health Potions")

# ROAMING

    elif commands == "1":

        print("You decided to explore the dungeon")
        time.sleep(0.5)
        print("Exploring...")
        time.sleep(1)

        roaming = random.choice(roam)

# FOUND NOTHING

        if roaming == "Nothing":
           print("You found an empty room!")
           continue

# FOUND LOOT

        elif roaming == "Loot":
           print("You found some loot: \n +1 Health Potion\n+15 Coins")
           player["coins"] += 15
           bag['Potions'] += 1

# ENCOUNTED GOBLIN

        elif roaming == "Goblin":
           
           goblin = Goblin()

           print("Careful!")
           time.sleep(0.5)
           print("You encountered an angry goblin!")
           time.sleep(0.3)
           print("Looks like you need to fight it somehow!")

# FIGHT MENU

           battling = True

           while battling:

            print(f"Your Health: {player['health']}\nGoblin Health: {goblin['health']}")
            fight = input("What will you do?\n1. Fight\n2.Bag\n3.Flee\n")
            

# BAG WHILE IN FIGHT

            if fight == "2":
                print(f"You have {bag['Potions']} Health Potions")

                if bag["Potions"] > 0:

                    potion_use = input("Would you like to use potion?\n1. Yes\n2. No\n")

                    if potion_use == "1":
                        print("You successfully used the potion")
                        bag["Potions"] -= 1
                        player["health"] += 15

                        if player["health"] > 100:
                            player["health"] = 100

                        print("The goblin attacked you!")
                        player["health"] -= goblin["attack"]

                        if player["health"] <= 0:
                                print("You Died")
                                time.sleep(0.5)
                                battling = False
                                running = False 
                                continue

                else:
                    print("No potion left")
                                
                    time.sleep(0.5)
                                    
                    continue

# FLEE FROM BATTLE

            elif fight == "3":
                print("You decided to flee from fight")
                time.sleep(0.6) 
                flee = random.choice(fleeing)

                if flee == "failed":
                    print("You failed to flee from battle")
                    time.sleep(0.5)
                        
                    print("The goblin attacked you!")
                    player["health"] -= goblin["attack"]

                    if player["health"] <= 0:
                            print("You Died")
                            time.sleep(0.5)
                            battling = False
                            running = False 
                            continue

                elif flee == "fleed":
                    print("You successfully fleed from battle!")
                    battling = False

# ATTACKING

            elif fight == "1":
                print("You decided to fight the goblin")
                time.sleep(0.4)

                print("You attacked the goblin!")

                luck = random.choice(battle_luck)

# SUCCESSFUL ATTACK

                if luck == "successful":
                    print("You successfully attacked the goblin!")

                    goblin["health"] -= player["attack"]

                    time.sleep(0.5)
                            
                    if goblin["health"] <= 0:
                        print("You killed the goblin!")

                                    
                        player["coins"] += 25

                        print("You got 25 coins from goblin!")
                        battling = False

                    else:

                        print("The goblin attacked you!")
                        player["health"] -= goblin["attack"]

                    print(f"Your Health: {player['health']}\nGoblin Health: {goblin['health']}")

                    if player["health"] <= 0:
                            print("You Died")
                            time.sleep(0.5)
                            battling = False
                            running = False 

# MISSED ATTACK

                elif luck == "missed":
                    print("You missed the attack!")
                            
                    time.sleep(0.5)
                            
                    print("The goblin attacked you!")
                    player["health"] -= goblin["attack"]

                    print(f"Your Health: {player['health']}\nGoblin Health: {goblin['health']}")

                    if player["health"] <= 0:
                        print("You Died")
                        time.sleep(0.5)
                        battling = False
                        running = False