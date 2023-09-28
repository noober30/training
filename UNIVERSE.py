import time
import os
from termcolor import colored
import random
import webbrowser
import sys

os.system('color 0a')

divider = "*"*30
name = ""
letters = "abcdefghijklmnopqrstuvwxyz".upper()
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
binary = "01"

#prerobit cely WARNING, zjednodusit
print("*"*24,"\n        WARNING!!!\nPlay at your own risk!!!") 
print("*"*24)
time.sleep(3)

def clearConsole():
    os.system("cls")

def wrongInput():
    clearConsole()
    print("Wrong input, Universe collapsing.\nEstimated time : few bilion years.")
    time.sleep(5)
    clearConsole()

def glitches(text):
    char_list = list(text)
    print(text)
    time.sleep(2)
    for _ in range(4,8):
        os.system("cls" )  
        char_list = list(text)
        random.shuffle(char_list)
        shuffled = "".join(char_list)
        print(shuffled, end="", flush=True)
        time.sleep(random.randint(0,2))
        clearConsole()
        print(text,end="", flush=True)
        time.sleep(1)
    clearConsole()
    print(text + "...")
    time.sleep(3)

def animate_text(text):
    number_of_characters=1
    while True:
        random_effect()
        print(text[0:number_of_characters])
        number_of_characters += 1
        if number_of_characters > len(text):
            number_of_characters = 0
            clearConsole()
        elif number_of_characters == len(text):
            clearConsole()
            print(text)
            time.sleep(5)
            break
    time.sleep(0.5)
    os.system('cls')

def random_effect():
    for i in range (10):
        random_letter = random.choice(letters)
        print(random_letter, end="\n", flush=True)
        time.sleep(0.1)
        clearConsole()  

def get_name():
    global name
    clearConsole()
    name_input = input("What`s your name? : ")
    if name_input.lower() == "neo" or name_input.lower() == "arthur":
        name = "The Chosen one"
    else:
        name = name_input

def intro():
    global name
    get_name()
    clearConsole()
    answer1 = input(f"Are you ready to find out the answer of Life, Universe and Everything, {name}?\ny/n: ".format(name))
    clearConsole()
    if answer1.lower() == "y":
        print("All right! Fasten your seatbelt and put on your VR glasses!")
        time.sleep(5)
        clearConsole()
        glasses()
        time.sleep(3)
        clearConsole()
        print("Welcome to...")
        time.sleep(2)
        logo()
        time.sleep(3)
        scene1()
    elif answer1.lower() == "n":
        gameOver()
    else:
        wrongInput()
        time.sleep(3)
        clearConsole()
        intro()  

def scene1():
    global name
    clearConsole()
    print("The Universe is a new VR game you`re about to try for the first time.\n")
    print("You never thought you would see a day where technology is so advanced,\nyou can play a game at home with the same experience as in reality.")
    time.sleep(10)
    print("\nBut here VR.",end="", flush=True)
    time.sleep(3)
    print(" ;)")
    time.sleep(3)
    clearConsole()
    city()
    print("\n\nYou`re in a neo-futuristic city, simmilar to cities that you know.")
    time.sleep(5)
    clearConsole()
    print(r'''
When your eyes adapt to the new enviroment,
you see a man approaching to you...''')
    time.sleep(3)
    print("\nYou start to recognize a familiar face...")
    time.sleep(5)
    clearConsole()
    aproachMorpheus()

def aproachMorpheus():
    global name
    Morpheus()
    print('"At last!"')
    print( f'"Welcome, {name}. As you no doubt have guessed, I am Morpheus."')
    time.sleep(3)
    print('"I`m freedom fighter as you, but you don`t know who you are, yet."')
    time.sleep(3)
    print('"Right now, we are in a simulation of life called..."')
    time.sleep(5)
    clearConsole()
    logo()
    time.sleep(3)
    print('\n"The real world is far from what it seems. "')
    time.sleep(3)
    clearConsole()
    print('"But I think, you`ve already noticed that..."')
    time.sleep(3)
    clearConsole()
    print('"Some misperceptions in this world..."')
    time.sleep(5)
    clearConsole()
    print('"Some..."')
    time.sleep(3)
    clearConsole()
    glitches("GLITCHES")
    first_choice()

def first_choice():
    global name
    clearConsole()
    print('Morpheus:\n\n"So, let\'s take a shortcut.')
    print('You take the blue pill, the story ends,\nyou wake up in your bed and believe whatever you want to believe.\n')
    time.sleep(5)
    print('You take the red pill, you stay in Wonderland,\nand I show you how deep the rabbit hole goes… \nRemember, all I’m offering is the truth, nothing more…"')
    time.sleep(5)
    answr = input("\nSo...Red or blue?\" : ")
    if answr.lower() == "blue":
        gameOver()
        morning()
    elif answr.lower() =="red":
        red_pill()
    else:
        clearConsole()
        glitches("WRONG CHOICE")
        first_choice()

def red_pill():
    global name
    clearConsole()
    print(f'\nMorpheus: "Wise choice, {name}. You\'ve chosen to see the truth."')
    time.sleep(3)
    print('"Prepare yourself for what comes next."')
    time.sleep(3)
    print("\nYou swallow the red pill, and your vision blurs...")
    time.sleep(3)
    print("\n\n--- Transitioning ---\n")
    time.sleep(3)
    clearConsole()
    print("Your mind drifts into darkness, and you find yourself floating in a sea of data.\n")
    time.sleep(5)
    print("Strange symbols and codes surround you, making no sense at first.\n")
    time.sleep(5)
    print("Gradually, you begin to understand them, and the truth starts to unveil.\n")
    time.sleep(7)
    clearConsole()
    print(f"You are {name}. The Chosen One. The One destined to break free from the virtual prison.\n")
    time.sleep(5)
    clearConsole()
    print("Memories from your real life flood back, and you remember your purpose.")
    time.sleep(5)
    print("Morpheus and his team guide you through simulations and combat training.")
    time.sleep(5)
    print("You learn how to bend the rules of The Universe, mastering your newfound abilities.")
    time.sleep(5)
    clearConsole()
    print("There's a long training filled with a lot of CGI`s effects.")
    time.sleep(5)
    print("\nMuch better than in Avengers Endgame.")
    time.sleep(7)
    print("\n♫♫♫ Eye of the tiger playing in the background. ♫♫♫")
    time.sleep(5)
    clearConsole()
    print("With each passing day, you grow stronger and more confident in your mission.")
    time.sleep(5)
    print("Finally, the time comes to confront the Architect, the creator of The Universe.")
    time.sleep(7)
    clearConsole()
    print("You enter the Mirror Room, prepared to face the ultimate challenge.")
    time.sleep(5)
    mirror_room()

def mirror_room():
    clearConsole()
    print("""Once you confront the Architect, you find youself in a vast, 
surreal chamber filled with complex geometric patterns and floating screens displaying lines of code.
The Architect, a sophisticated AI, speaks in an emotionless and condescending tone.\n 
He explains that you are not the first "One" to emerge, but merely one of many who have been chosen 
to reboot the Matrix when it becomes unstable.""")
    time.sleep(15)
    clearConsole()
    mirror_room_answr()

def mirror_room_answr():
    global name
    answr1 = input("Do you want to FIGHT Architect or RESTART Matrix? : ") 
    if answr1.lower() == "fight":
        architect_fight1()
    elif answr1.lower() == "restart":
        clearConsole()
        print("""The fake world that Neo and the other humans have known begins to disintegrate around
them. Buildings crumble like sandcastles, and the once familiar landscapes distort into abstract shapes.
The entire virtual reality becomes a chaotic digital storm as the Matrix undergoes a complete reset.""")
        time.sleep(15)
        effect(alphabet)
        morning()
    else:
        wrongInput()
        time.sleep(3)
        clearConsole()
        mirror_room_answr()

def architect_fight1():
    global name
    clearConsole()
    print(f'"Fighting me won\'t be easy for you, {name}. Never was, never will be."')
    time.sleep(5)
    print('''\n"To advance further, you must decipher the color code before you. 
Each colored tile represents a specific numerical value, and you must determine the correct sequence of light
to unlock the next challenge."''')
    time.sleep(7)
    red = colored("\n1 : Red", "red")
    green = colored("\n2 : Green", "green")
    blue = colored("\n3 : Blue", "blue")
    yellow = colored("\n4 : Yellow", "yellow")
    white = colored("\n5 : White", "white")
    print(red, green, blue, yellow, white)
    time.sleep(5)
    answr = input("\033[32m\nWrite numerical code: ")
    answr = answr.replace(" ","")
    if answr == "123":
        clearConsole()
        os.system('color 0a')
        print("That was easy! Next cipher won't be.")
        time.sleep(3)
        architect_fight2()
    else: 
        wrongInput()
        print("\033[32mHint: The sequence of colors is related to the primary colors of light...")
        time.sleep(5)
        architect_fight1()

def architect_fight2():
    global name
    clearConsole()
    print('''Architect: "In this challenge, you must decipher the enigmatic sequences to unlock the path forward.
Each sequence conceals a hidden numerical value, and you must decipher the correct sequence
to reveal the answer."''')
    time.sleep(3)
    print()
    print("[ 1 ]  [ 1 ]  [ 2 ]  [ 3 ]  [ 5 ]")
    time.sleep(3)
    print()
    print('''Architect: "To determine the hidden numerical value, you must comprehend the pattern 
within the sequence. Each number in the sequence is obtained through a unique progression."''')
    time.sleep(3)
    print('''\nFind the next number in the sequence to unlock the hidden value.''')
    time.sleep(3)
    answr = input("\nWrite next number : ")
    if answr == "8":
        clearConsole()
        print('"Uncalculatable! But you\'re right. Let\'s move on."')
        time.sleep(5)
        architect_fight3()
    else:
        wrongInput()
        print("It appears to be the Fibbonacci's sequence...")
        time.sleep(3)
        architect_fight2()

def architect_fight3():
    global name
    clearConsole()
    print(f'"Just last cipher awaits you, {name}."')
    time.sleep(3)
    clearConsole()
    print('"Now I don\'t want the answer, I want you to ask me the right QUESTION."')
    time.sleep(7)
    clearConsole()
    print('"Answer to this ultimate QUESTION is known for bilions of years.\nIt was calculated 7.5 bilion years ago by computer known as DEEP THOUGHT.\n\nThe answer to life, Universe and everything."')
    time.sleep(15)
    clearConsole()
    print('"If you never heard of it, open this link and ask about it the Universal knowledge: \nhttp://www.usethefuckinggoogle.com/?q=answer+to+life%2C+universe+and+everything"')
    time.sleep(10)
    clearConsole()
    print('"This task looks easy. I will give you a program, which is choosing some TOTALLY RANDOM letters and make a RANDOM sentence... "') #and THE UNIVERSE will do the rest.
    time.sleep(7)
    print("\nSO YOU WILL NEVER FIND OUT THE RIGHT QUESTION!!!")
    time.sleep(5)
    print("\nMUHAHAHAHAHA!!!!!\n\nYOU THOUGHT I'M STUPID?????")
    time.sleep(5)
    clearConsole()
    print('"The question and answer can\'t exist in the same UNIVERSE at the same time!!!"'.upper())
    time.sleep(5)
    print('\n"Some people say, that if ever anyone discovers the exact question and exact answer what the Universe is for and why it is here,\nit will instantly disappear and be replaced by something even more bizarre and inexplicable."'.upper())
    time.sleep(15)
    clearConsole()
    print('"There is another theory, which states that this has already happened." ')
    time.sleep(10)
    last_scene()

def last_scene():
    global name
    clearConsole()
    print(f'"Let\'s start, {name}"')
    time.sleep(3)
    print('"And end this misery."')
    time.sleep(5)
    animate_text("WHAT YOU GET WHEN YOU MULTIPLY 6 BY 9?")
    time.sleep(3)
    shut_down()

def shut_down():
    global name
    clearConsole()
    print('Architect: "THIS IS WRONG"')
    time.sleep(3)
    print('\n"THIS IS NOT SUPPOSED TO BE THE RIGHT ANSWER!"')
    time.sleep(3)
    print("That does\n't make sense!!!".upper())
    clearConsole()
    glitches("UNCALCULATABLE")
    effect(binary)
    answer_to_everything()

def effect(symbols):
    tm = 0
    while tm < 30:
        print(" ".join(random.choice(symbols) + random.randrange(1, 5) * " " for _ in range(50))
        )
        tm = tm + 0.1
        time.sleep(0.1)

def gameOver():
    clearConsole()
    print("All right, sweet dreams. We`ll meet in your next existence.")
    time.sleep(5)
    morning()

def morning():
    clearConsole()
    print("You wake up in your room with no memories.\nIt`s every day morning, same as ever, except for the ocassional glitches, like Déjà Vu...")
    time.sleep(7)
    clearConsole()
    glitches("Déjà Vu")
    time.sleep(3)
    clearConsole()
    print("Your phone is ringing and it's the courier service. You don't remember ordering anything...")
    time.sleep(5)
    print("\nIt's a game. And today is a free day...")
    time.sleep(5)
    clearConsole()
    glasses()
    print("You put on your VR glasses.")
    time.sleep(5)
    clearConsole()
    city()
    print("\n\nYou`re in a neo-futuristic city, simmilar to cities that you know.")
    time.sleep(5)
    clearConsole()
    print(r'''
When your eyes adapt to the new enviroment,
you see a man approaching to you...''')
    time.sleep(3)
    print("\nYou start to recognize a familiar face...")
    time.sleep(5)
    clearConsole()
    aproachMorpheus()

def answer_to_everything():
    clearConsole()
    webbrowser.open("https://www.youtube.com/watch?v=aboZctrHfK8")
    time.sleep(1) #zmenit na 180, snad si to niekto preklikne po videu naspat
    print("The computer that contains organic life and is currently calculating the ultimate question to life, Universe and everything is called...")
    time.sleep(10)
    clearConsole()
    print("THE EARTH")
    time.sleep(7)
    clearConsole()
    print("And Earth... is in the UNIVERSE...")
    time.sleep(10)
    clearConsole()
    glitches("THE END") #add blinking question mark at the end
    clearConsole()
    sys.stdout.write("THE END...  ")
    sys.stdout.flush()
    time.sleep(3)
    for _ in range(100):
        sys.stdout.write("\b?")
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write("\b ")
        sys.stdout.flush()
        time.sleep(1)
    # PLAY AGAIN? OK - turning off the computer :D

def logo():
    print(r'''  _____ _            _   _       _                         
 |_   _| |__   ___  | | | |_ __ (_)_   _____ _ __ ___  ___ 
   | | | '_ \ / _ \ | | | | '_ \| \ \ / / _ \ '__/ __|/ _ \
   | | | | | |  __/ | |_| | | | | |\ V /  __/ |  \__ \  __/
   |_| |_| |_|\___|  \___/|_| |_|_| \_/ \___|_|  |___/\___|
                                                           ''') 

def Morpheus():
    print(r'''               __
            .'  `'.
           /  _    |
           #_/.\==/.\
          (, \_/ \\_/
           |    -' |
           \   '=  /
           /`-.__.'
        .-'`-.___|__
       /    \       `.''' )
    
def city():
    print(r'''           W            __  __
          [ ]          |::||::|
           3   ._.     |::||::|   ._.
          /|   |:| ._. |::||::|   |/|
      \|// /   |:|_|/| |::||::|_  |/|
     -( )-|    |:|"|/|_|::||::|\|_|/| _
      J V |    |:|"|/|||::||::|\|||/||:|
___  '    /  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\  \/    |        ~~~ ~~~ ~~~~~ ~~~~~''')
    
def glasses():
    print(r'''    __         __
   /.-'       `-.\
  //             \\
 /j_______________j\
/o.-==-. .-. .-==-.o\
||      )) ((      ||
 \\____//   \\____//   
  `-==-'     `-==-'   
          ''') 

# some years ago, virtual reality was an escape from the real world
# today the real world is an escape from the virtual reality 
    
intro()