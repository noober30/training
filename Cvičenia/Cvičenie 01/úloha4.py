import datetime

yearnow = datetime.datetime.now().year
name = input("Zadaj svoje meno:   ")
birthdate = int(input("Zadaj rok narodenia:   "))
adress = input("Zadaj krajinu kde bývaš:   ")
age= yearnow-birthdate

print("=" * 20 + "\nMeno: " + name + "\nVek: " + str(age) + "\nAdress: " + adress + "\n" + "=" * 20)




