import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear') # idk if we should use this but ill keep it in
print("GregHack Command Prompt")
print("Hi! Sorry, I should introduce myself. I'm the game.")
print("Your task is to hack into Bob's account.")
print("Go to https://greghack.freakybob.site and click on BaseLook.")
print("It'll bring you to Bob's BaseLook.")
print("Now, type infosearch")
cmd = input()
    
if (cmd.lower() == "help"):
    print("hack - hacking tool if you have all info")
    print("infosearch - search for info about people")
    cmd = input()
    
if (cmd.lower() == "infosearch"):
    print("infosearch - very legal fr")
    print("hint: Ym9i")
    print("Great! Enter bob into the prompt below.")
    name = input("name of person: ")
    if (name == "bob"):
        print("Searching...")
        print("Found!")
        print("bob's BaseLook password found. catsarecool123")
        print("Now, enter hack.")

if (cmd.lower() == "hack"):
    print("Nice! Enter bob as the username and the password you got from infosearch.")
    user = input("enter username: ")
    password = input("enter password: ")
    if ("bob" in user):
        if (password == "catsarecool123"):
            print("Beep boop. Bob has been hacked.")
            print("You did it!")
            print("GregSend: You got pinged in Friends. 'Greg! Check the news, now!'")
            print("Go back to the greghack website and click on the browser!")