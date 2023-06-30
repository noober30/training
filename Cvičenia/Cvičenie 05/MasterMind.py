import random
import time
from colorama import init, Fore, Style
init()
print()
print()

name = input("Meno hráča  :  ")
if name == "":
    name = "Player1"
logo = """.___  ___.  _______   _______      ___      .___  ___.  __  .__   __.  _______  
|   \/   | |   ____| /  _____|    /   \     |   \/   | |  | |  \ |  | |       \ 
|  \  /  | |  |__   |  |  __     /  ^  \    |  \  /  | |  | |   \|  | |  .--.  |
|  |\/|  | |   __|  |  | |_ |   /  /_\  \   |  |\/|  | |  | |  . `  | |  |  |  |
|  |  |  | |  |____ |  |__| |  /  _____  \  |  |  |  | |  | |  |\   | |  '--'  |
|__|  |__| |_______| \______| /__/     \__\ |__|  |__| |__| |__| \__| |_______/ """

print()
print()

end = """  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______       __  
 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     |  | 
|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    |  | 
|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     |  | 
|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.|__| 
 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|(__) """
                                                                                                  
print(logo)

print()
print()
                                                                
print("Vitaj v hre {}!\nAk chceš skončiť, hocikedy napíš `koniec`.\nUhádni číslo od 0 do 100, na ktoré myslím:\n\nMyslím si číslo...".format(name))
time.sleep(2)
print()

#Loading screen
for i in range(1):
    print("Premýšľam", end="")
    for j in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print()

time.sleep(2)
print()
print("Už ho mám!!!")
print()
time.sleep(1)

score = 0
wrong = 0
rand = random.randint(0,100)

while True:
    print()
    tip = input("Tvoj tip? : ")
    if tip.isdigit():
        tip = int(tip)
        if tip == rand:
            print("\033[32mÁNO!!!\033[0m")
            score += 1
            rand = random.randint(0,100)
            ask = input("\nChceš hrať ďalej? Ak áno, napíš [y], ak nie [n]  :  ")
            if ask.lower() == "y":
                print(logo)
                continue
            elif ask.lower() == "n":
                print (end)
                break
            if ask != "y" or ask != "n":
                print("\nNepoznáš abecedu? Takže pokračuješ!")   #neviem sa dostať na spat na ask
                continue
        else:
            wrong += 1
            if int(tip) < rand:
                print("Číslo ktoré si myslím, je väčšie!")
            if int(tip) > rand:
                print("Číslo ktoré si myslím, je menšie!") 
                continue               
    elif tip.upper() == "KONIEC":
        print (end)
        break
    else:
        print("Zadaj číslo alebo 'koniec'!")
        continue

print("\n"*2)
print(("="*20) + f"\nPočet tipov: {wrong}\nPočet uhádnutí: {score}\n" + ("="*20))
print("\n"*2)









    

      


    
    



