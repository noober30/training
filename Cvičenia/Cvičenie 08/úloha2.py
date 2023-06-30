subor = open(input("Zadaj meno súboru : "),"r")

riadky = 0
znaky1 = 0
longest = []

for line in subor:
    riadky += 1
    for znak in line:
        if znak != "\n":
            znaky1 += 1
    longest.append(znaky1)
    znaky1 = 0

print(f"Meno súboru : {subor.name} \nNajdlhší má {max(longest)} znakov\nPočet riadkov súboru je : {riadky}")


subor.close()

