import random
import sys
import os
import modules.items as items

bullets = []
enemyLives = 3
playerLives = 3

def calculate_percentage(num1, num2):
    return (num1 / num2)

def bulletRandomiser():
    for i in range(random.randint(4, 8)):
        bullets.append(random.choice([True, False]))

def checkBullets():
    if len(bullets) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nThere are no more bullets left therefore the shotgun is reloaded")
        bulletRandomiser()
        print(f"There are {sum(bullets)}/{len(bullets)} which are not duds.")
    else:
        pass

def enemyChoice():
    #We are not adding any AI into this game instead we are providing simple logic.
    #We will also provide a True/False value where if True it will shoot the player otherwise itself.
    return random.choices([True, False], weights=[calculate_percentage(sum(bullets), len(bullets)), calculate_percentage(len(bullets) - sum(bullets), len(bullets))])[0]

def commandList():
    print("""
These are the commands you are able to do:
- shoot {enemy/yourself}
- help
- exit""")

def checkLives():
    if enemyLives == 0:
        print("\nThe enemy has no more lives; You have won")
        sys.exit()
    if playerLives == 0:
        print("\nYou have lost")
        sys.exit()
    else:
        pass

def shoot(player, character):
    global enemyLives
    global playerLives
    global bullets

    if bullets[0]:
        if player == character:
            if "player" in player:
                playerLives -= 1
                print(f"You shot yourself; You now have {playerLives} lives left\n")
                bullets.pop(0)
            if "enemy" in player:
                enemyLives -= 1
                print(f"The enemy shot itself; They now have {enemyLives} lives left\n")
                bullets.pop(0)
        else:
            if character == "player":
                playerLives -= 1
                print(f"The enemy shot you; You now have {playerLives} lives left!\n")
                bullets.pop(0)
            if character == "enemy":
                enemyLives -= 1
                print(f"You shot the enemy; They now have {enemyLives} lives left!\n")
    else:
        print(f"The shotgun was aimed at {character} by {player} but nothing happened\n")
        bullets.pop(0)

bulletRandomiser()
print(f"""
Welcome to the game of Buckshot Roulette!
There is a shotgun in front of you with a creature waiting for you to get ready.
Only one will leave alive

There are {sum(bullets)}/{len(bullets)} which are not duds.
You both start with 3 lives.

What will you do?""")

commandList()

def gameplay():
    checkLives()
    checkBullets()
    global enemyLives
    global playerLives
    global bullets
    playerTurn = True

    userInput = input("\n> ")

    if "help" == userInput.lower() and playerTurn:
        commandList()

    if "exit" == userInput.lower() and playerTurn:
        sys.exit()

    if "shoot" in userInput.lower() and playerTurn:
        if "enemy" in userInput.lower():
            shoot("player", "enemy")
            playerTurn = False
        elif "yourself" in userInput.lower():
            shoot("player", "player")
            playerTurn = False
        else:
            print("I am unsure who you want to shoot")

    checkLives()
    checkBullets()

    if not playerTurn:
        if enemyChoice():
            shoot("enemy", "player")
            playerTurn = True
        else:
            shoot("enemy", "enemy")
            playerTurn = True

    checkLives()
    checkBullets()

while True:
    gameplay()