# Úloha 1
# vezmi riešenie z predchádzajúceho riešenia s formátovaním stringov a
# vykreslovaním kocky. Tentokrát použi modul random na získanie náhodného
# čísla. Vytvor podmienky typu "elif" a vykresli správnu stranu kocky. Na
# vykreslenie použi iba funkciu "format" a "print"

import random
num= random.randint(1,6)

dice= "+-------+ \n|{val1}  {val2}  {val3}|\n|{val4}  {val5}  {val6}|\n|{val7}  {val8}  {val9}|\n+-------+"

if num == 1:
    print(dice.format (val1= " ", val2 = " ", val3 =" ", val4 = " ", val5 = "*", val6= " ", val7=" ", val8=" ",val9=" "))
elif num ==2:
    print(dice.format (val1= " ", val2 = "*", val3 =" ", val4 = " ", val5 = " ", val6= " ", val7=" ", val8="*",val9=" "))
elif num ==3:
    print(dice.format (val1= " ", val2 = "*", val3 =" ", val4 = " ", val5 = "*", val6= " ", val7=" ", val8="*",val9=" "))
elif num ==4:
    print(dice.format (val1= "*", val2 = " ", val3 ="*", val4 = " ", val5 = " ", val6= " ", val7="*", val8=" ",val9="*"))
elif num ==5:
    print(dice.format (val1= "*", val2 = " ", val3 ="*", val4 = " ", val5 = "*", val6= " ", val7="*", val8=" ",val9="*"))
else:
    print(dice.format (val1= "*", val2 = "*", val3 ="*", val4 = " ", val5 = " ", val6= " ", val7="*", val8="*",val9="*"))











