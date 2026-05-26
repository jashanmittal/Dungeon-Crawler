import random
import time
running = True
# extra
loot = "coins", "potion"
event = "goblin", "loot", "nothing"
gp = "attack", "miss"

# player
health = 100
attack = 15
coins = 0
potion = []

# main
print("******************************")
print("You Have Entered The Dungeons!")
print("******************************")
print()

while running:
    
    # goblin
    g_health = 60
    g_attack = 20

    print("Which action would you do?")
    print()
    command = input("1. Move ahead\n2. Escape\n3. Check Bag:\n")

    if command == "2":
        break

    elif command == "3":
        print(f"You have {coins} coins and {potion} potions")
    
    elif command == "1":
        print("You decided to move ahead!")
        time.sleep(1)

        print("Exploring...")
        time.sleep(1.5)

        choosen_event = random.choice(event)

        if choosen_event == "nothing":
            print("You found nothing")
            continue
        
        if choosen_event == "loot":
            print("You found some loot lying!")
            coins += 10
            potion.append("Health Potion")
            continue

        if choosen_event == "goblin":
            print("You encounted a Goblin!")
            battle = True
            
            while battle:
                if choosen_event == "goblin":
                    print(f"Goblin's Health: {g_health}")
                    print("What will you do?")

                    user = input("1. Attack\n2. Potion:\n")

                    if user == "1":
                        print ("You attacked goblin with sword")
                        time.sleep(1.5)
                        action = random.choice(gp)

                        if action == "miss":
                            print("You missed the attack")
                            time.sleep(1)

                            print("Goblin attacked you!")
                            time.sleep(1)
                            health -= 20
                            print(f"Your health is: {health}")
                            continue

                        elif action == "attack":
                            print("You attacked the goblin with sword successfully")
                            g_health -= 15
                            print(f"Goblin's Health: {g_health}")
                            if g_health <= 0:
                                print("You defeated the goblin")
                                time.sleep(0.5)
                                print("You recieved 20 coins")
                                coins += 20
                                battle = False
                                break

                            time.sleep(1)

                            print("Goblin attacked you!")
                            time.sleep(1)
                            health -= 20
                            print(f"Your health is: {health}")
                            
                        if health <= 0:
                            print("You Died from Goblin!")
                            battle = False
                            running = False
                    continue
