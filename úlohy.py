veta = input("Zadaj vetu:     ")
listSlov= veta.split()
print(listSlov)
počet = 0
for i in range(len(listSlov)):
   for y in range(len(listSlov)):
      if listSlov[i] == listSlov[y]:
         počet += 1

   print(listSlov[i] + " Počet slova je:    " + str(počet))      
   počet = 0        






   

       