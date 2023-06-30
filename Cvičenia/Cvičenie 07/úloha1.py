num =  25

def list_all_divisors(num):
    for i in range(1,num+1):
        if num %i == 0:
            print (i,end=" ")

list_all_divisors(num)




