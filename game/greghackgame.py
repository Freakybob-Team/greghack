import os
import inquirer
import requests

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
                choices=['Start and Download Levels', 'Exit'],
            ),
]

answers = inquirer.prompt(menu)

if (answers['start'] == "Start and Download Levels"):
    print("This will download Level 1 for playing.")
    url = 'https://github.com/Freakybob-Team/greghack/blob/main/game/levels/level1.py?raw=true'
    response = requests.get(url)
    file_Path = "levels/level1.py"
    response = requests.get(url)

    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
            print('File downloaded successfully')
    else:
        print("Oops! There was an error and we couldn't download LigmaBalls.")
    print("Done! Level one has been downloaded from https://github.com/Freakybob-Team/greghack/tree/main/game/levels/level1.py")
    exec(open('levels/level1.py').read())