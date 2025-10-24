import os
import sys
try:
    import inquirer
except:
    print("Please install inquirer with pip install inquirer!")
    print("GregHack will now quit.")
    sys.exit()
import urllib.request

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print("please visit greghack.freakybob.site for everything else, like clues to play, as this game is just a console")
# greghack.freakybob.site is now used for information AND the game
print("DISCLAIMER: This is not a real hacking tool and does not affect any real website or person.")
input("I have visited the website greghack.freakybob.site, as I must use it to play the game.")

cls()
print("Greg OS Command Prompt")
print("Version 1.25") # increase first number every release, increase second number every year (ex: 1.25, 1 being release number, and 25 being year)

menu = [
  inquirer.List('start',
                message="GregHack Launcher by Freakybob Team",
                choices=['Start','Download Levels', 'Exit'],
            ),
]

answers = inquirer.prompt(menu)

if (answers['start'] == "Download Levels"):
    print("This will download Level 1 for playing.")
    if os.path.exists("levels/"):
        os.mkdir("levels/")
    try:
        urllib.request.urlretrieve("https://github.com/Freakybob-Team/greghack/blob/main/game/levels/level1.py?raw=true", "levels/level1.py")
        urllib.request.urlretrieve("https://github.com/Freakybob-Team/greghack/blob/main/game/levels/lvl.py?raw=true", "levels/lvl.py")
    except:
        print("Oops! There was an error and we couldn't download GregHacks levels.")
    print("Done! Levels were downloaded.")
    exec(open('levels/lvl.py').read())

if (answers['start'] == "Start"):
    print("Have fun! :)")
    exec(open('levels/lvl.py').read())