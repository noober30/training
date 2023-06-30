A = {1: "one", 2: "two"}
B = {2: "dva", 3: "three"}

C = A

for key, value in B.items():
    if key in C:
        C[key] = [C[key], value]
    else:
        C[key] = value

print(C)




