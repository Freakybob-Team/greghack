import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cmd = None
print("greghack")
print("by freakybob team")
print("please visit greghack.freakybob.site for everything else, like clues to play, as this game is just a console")
print("game.freakybob.site/greghack for information about the game")
print("DISCLAIMER: This is not a real hacking tool and does not affect any real website or person.")
input("I have visited the website greghack.freakybob.site, as I must use it to play the game.")
cls()
print("Greg OS Command Prompt")
print("Version 1.25") # increase first number every release, increase second number every year (ex: 1.25, 1 being release number, and 25 being year)
print("Type help for help.")
cmd = input()
if (cmd == "hack"):
    cls()
    user = input("enter username: ")
    website = input("enter website: ")
if (cmd == "help"):
    cls()
    print("hack - hacking tool if you have all info")
    print("infosearch - search for info about people")
    cmd = input()