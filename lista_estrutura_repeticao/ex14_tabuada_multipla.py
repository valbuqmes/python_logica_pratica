#Leia dois inteiros A e B (A <= B). Para cada número entre A e B, exiba sua tabuada completa (1 a 10).
#Separe cada tabuada com uma linha tracejada. Use laços aninhados.

a = int(input("Digite: "))
b = int(input("Digite: "))


for i in range(a, b+1):
    for n in range(1, 10+1):
        print(f"{i} * {n} = {i*n}")
    
    print("----------------------------")