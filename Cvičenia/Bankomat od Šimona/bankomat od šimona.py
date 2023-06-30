import random
import sys, os

name  = ["admin", "simon"]
psswrd = ["admin", "simon"]
bankNum = ["", "12345"]
state = ["", "SK"]
status = [0, 0]

adminName = name[0]
adminPass = psswrd[0]

username = ""

def clearConsole():
    os.system('cls')

def wrongPass():
    clearConsole()
    print("Wrong password\nPress enter")
    input()
    login()

def confirmPass(INname):
    global username, psswrd, name
    index = name.index(INname)
    if psswrd[index] == input("password: "):
        username = INname
        menu()
    else:
        wrongPass()

def getIndexByName(INname):
    global name
    if INname in name:
        return name.index(INname)
    else:
        clearConsole()
        print("Account dont exist.")
        input("Press ENTER to exit.")
        menu()

def getIndexByBankNum(INbankNum):
    global bankNum
    if INbankNum in bankNum:
        return bankNum.index(INbankNum)
    else:
        clearConsole()
        print("Account dont exist.")
        input("Press ENTER to exit.")
        menu()

def printUserInfo(index):
    global name, psswrd, state, bankNum, status
    clearConsole()
    print("name: " + name[index] +"\npassword: "+ psswrd[index] +"\nstate: "+ state[index] +"\naccount number: "+ bankNum[index] + "\nstatus: " + str(status[index]))

def GenerateBankNum():
    global bankNum
    while True:
            x = str(random.randint(1, 999999)).zfill(6)
            if x not in bankNum:
                break
    return x

def deleteAccount(INname):
    global name, psswrd, state, bankNum, status, username
    cont = input("Do you want to Log out (y/n): ")
    if cont == "y" or cont == "Y":
        index = getIndexByName(INname)
        name.pop(index)
        psswrd.pop(index)
        state.pop(index)
        bankNum.pop(index)
        status.pop(index)
    else:
        menu()

def menu():
    global username, adminName
    welcome = "Welcome to Bank Management System"
    action = "Please select an action:"
    clearConsole()

    if username != "" and username != adminName:
        print(welcome + "\n" + action)
        print("1.) View account details")
        print("2.) Deposit money")
        print("3.) Withdraw money")
        print("4.) send money")
        print("5.) Close account")
        print("6.) Log out\n")
    if username == adminName:
        print(welcome + "\n" + action)
        print("1.) View accounts")
        print("2.) View account details")
        print("3.) Log out\n")
    if username == "":
        print(welcome + "\n" + action)
        print("1.) Log in")
        print("2.) Register\n")
    handler()

def handler():
    global username, adminName
    answr = input("Choose your action: ")
    if username != "" and username != adminName:
        if answr == "1":
            viewAccountInfo()
        if answr == "2":
            moneyAction("d")
        if answr == "3":
            moneyAction("w")
        if answr == "4":
            moneyAction("s")
        if answr == "5":
            closeAccount()
        if answr == "6":
            logout()
        else:
            input("wrong action\nPress ENTER to continue")
            menu()
    if username == adminName:
        if answr == "1":
            viewAccounts()
        if answr == "2":
            viewAccountInfo()
        if answr == "3":
            logout()
        if answr == "4":
            closeAccount()
        else:
            input("wrong action\nPress ENTER to continue")
            menu()
    if username == "":
        if answr == "1":
            login()
        if answr == "2":
            register(name, psswrd, state, bankNum, status)
        else:
            input("wrong action\nPress ENTER to continue")
            menu()
        
def register(name: list, psswrd: list, state: list, bankNum: list, status: list):
    clearConsole()
    cont = input("Do you want to continue (y/n): ")
    if cont == "y" or cont == "Y":
        clearConsole()
        print("Please fill in your info.\n")
        INname  = input("Name: ")
        INpsswrd = input("Password: ")
        INstate = input("State (SK): ")
        INstatus = 0
        INbankNum = GenerateBankNum()
        clearConsole()
        print("name: " + INname +"\npassword: "+ INpsswrd +"\nstate: "+ INstate +"\naccount number: "+ INbankNum)
        agree = input("Do you agree to registration (y/n)")
        if agree == "y" or agree == "Y":
            clearConsole()
            name.append(INname)
            psswrd.append(INpsswrd)
            state.append(INstate)
            bankNum.append(INbankNum)
            status.append(INstatus)
            menu()
        else: 
            register(name, psswrd, state, bankNum, status)
    else: 
        menu(username)

def login():
    global psswrd, name
    clearConsole()
    print("Log-In or type in \"c\" for cancle")
    INname = input("name: ")
    if INname != "c":
        confirmPass(INname)
    else:
        menu()

def viewAccounts():
    global name
    clearConsole()
    print(name)
    input("Press ENTER to exit.")
    menu()

def viewAccountInfo():
    global username, adminName
    clearConsole()
    if username == adminName:
        printUserInfo(getIndexByName(input("Enter client name: ")))
        input("Press ENTER to exit.")
        menu()
    else:
        printUserInfo(getIndexByName(username))
        input("Press ENTER to exit.")
        menu()

def logout():
    global username
    clearConsole()
    cont = input("Do you want to Log out (y/n): ")
    if cont == "y" or cont == "Y":
        username = ""
        menu()
    else:
        menu()
    
def closeAccount():
    global name, psswrd, state, bankNum, status, username, adminName
    if username == adminName:
        clearConsole()
        user = input("account to delete: ")
        clearConsole()
        deleteAccount(user)
        menu()
    else:
        clearConsole()
        deleteAccount(username)
        username = ""
        menu()
    
def moneyAction(action):
    global status, username
    index = getIndexByName(username)
    clearConsole()
    val = input("Enter price or \"c\" for cancel action: ")
    if val == "c" or val == "C":
        menu()
    else:
        clearConsole()
        if action == "w":
            if int(val) > status[index]:
                print("not enough funds!")
            else:
                status[index] -= int(val)    
        if action == "d":
            status[index] += int(val)
        if action == "s":
            sendMoney(input("Enter the account number of your recievers account: "), val)
        print("status: " + str(status[index]))
        input("Press ENTER to exit.")
        menu()

def sendMoney(reciever, money):
    global status, username, name
    Rindex = getIndexByBankNum(reciever)
    Uindex = getIndexByName(username)
    clearConsole()
    print("account name: " + name[Rindex])
    val = input("Continue? (y/n) : ")
    if val == "n" or val == "N":
        menu()
    else:
        if int(money) > status[Uindex]:
            print("not enough funds!")
        else:
            status[Uindex] -= int(money)
            status[Rindex] += int(money)
            clearConsole()
            print("payment SUCCESSFUL")

menu()