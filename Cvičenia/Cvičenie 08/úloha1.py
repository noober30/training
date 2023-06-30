name = input("Zadaj meno súboru : ")

with open(name,"r") as subor:
    print(subor.read(3))