import sys
import time
import os
try:
    import inquirer
except:
    print("Please install inquirer with pip install inquirer!")
    print("GregHack will now quit.")
    sys.exit()

print("Welcome to the Level Manager")
print("What level would you like to play?")

menu = [
  inquirer.List('start',
                message="Levels",
                choices=['Tutorial (Level 1)'],
            ),
]

answers = inquirer.prompt(menu)

if (answers["start"] == "Tutorial (Level 1)"):
    print("Okay! Have fun :)")
    print("I'm going to clear your terminal in 3 seconds, and then launch the game.")
    time.sleep(3)
    os.system('cls' if os.name=='nt' else 'clear')
    exec(open('levels/level1.py').read())