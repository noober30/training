veta = input("Zadaj vetu:     ")
počet = 0
maxPočet = ""
predPoč = 0

for i in range(len(veta)):
    for y in range(len(veta)):
        if veta[i] == veta[y]:
            počet += 1
    if počet > predPoč:
        maxPočet = veta[i]
        predPoč = počet
    počet = 0
print (maxPočet +  " : " + str(predPoč))    
   
