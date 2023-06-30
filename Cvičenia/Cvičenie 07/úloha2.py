def list_all_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def is_perfect(num):
    divisors = list_all_divisors(num)
    sucet = sum(divisors[:-1])
    return sucet == num               

result = is_perfect(27)    #nerozumiem preco mi nevracalo true alebo false, opravil som to cez premennu result 
print(result)
