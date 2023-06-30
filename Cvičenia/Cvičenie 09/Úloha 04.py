#Napíš rekurzívnu funkciu pocet(znak, retazec), ktorá bez cyklu a reťazcových metód 
#zistí počet výskytov zadaného znaku vo vstupnom reťazci.

def pocet(char, veta):
    if char.lower() not in veta.lower():
        return 0
    return veta.lower().count(char.lower())
        

print(pocet("mA", "MamA Ma EMU, eMa ma MamU"))
