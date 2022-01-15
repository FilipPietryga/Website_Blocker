from time import *
from datetime import *

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "https://www.facebook.com"]
mode = "onwill"

def mainmenu():
    print("Welcome to the website blocker!!\n\n")
    print("What would you do")
    print("1. Continue")
    print("2. Settings")
    print("3. Exit")
    option = int(input("Choose option"))
    if(option == 1):
        pass
    elif(option == 2):
        if(option == 1):
            print("1. Add a website")
            print("2. Remove a website")
            print("3. Exit")
            option = int(input("choose option"))
            if(option == 1):
                name = input("insert link to the website that you want to block")
                websites.append(name)
            elif(option == 2):
                index = 1
                for website in websites:
                    print(index + ". " + website)
                which = int(input("which website would you like to remove from the list"))
                websites.remove(websites[which])
            elif(option == 3):
                pass
            else:
                print("wrong input")

        elif(option == 2):
            print("1. Block on time")
            print("2. Block on will")
            print("3. Exit")
            option = int(input("choose option"))
            if(option == 1):
                mode = "ontime"
                print("on which hours would you like the program to block websites?")
                start = int(input(""))
            elif(option == 2):
                mode = "onwill"
            elif(option == 3):
                pass
            else:
                print("wrong input")
        elif(option == 3):
            pass
        else:
            print("wrong input")
    elif(option == 3):
        exit()
    else:
        print("wrong input")

while True:
    mainmenu()
    if(mode == "onwill"):
        print("Would you like to block websites or unlock them? (block/unlock)")
        option = input()
        if(option == "block"):
            print("the websites got blocked")
            with open(host_path, "r+") as fileptr:
                content = fileptr.read()
                for website in websites:
                    if website in content:
                        pass
                    else:
                        fileptr.write(redirect + " " + website + "\n")
        elif(option == "unlock"):
            print("the websited got unlocked")
            with open(host_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites):
                        file.write(line)
                file.truncate()
        else:
            print("wrong input")

    if(mode == "time"):
        print("Time blocking turned on")
        _datetime = datetime.now();
        if(datetime(_datetime.year, _datetime.month, _datetime.day, 2) 
        < _datetime < 
        datetime(_datetime.year, _datetime.month, _datetime.day, 3)):
            print("Working hours")
            with open(host_path, "r+") as fileptr:
                content = fileptr.read()
                for website in websites:
                    if website in content:
                        pass
                    else:
                        fileptr.write(redirect + " " + website + "\n")
        else:
            print("Fun hours")
            with open(host_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites):
                        file.write(line)
                file.truncate()
    sleep(5)