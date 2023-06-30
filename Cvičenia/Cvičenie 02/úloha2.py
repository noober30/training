num = int(input("Zadaj číslo :"))
print( bin(num).replace("0b","").zfill(32))
