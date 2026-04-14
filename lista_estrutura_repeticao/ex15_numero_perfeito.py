#Leia um inteiro N maior que 1. Um número perfeito é igual à soma de seus divisores próprios (ex: 6 =
#1+2+3). Verifique e exiba se N é perfeito ou não perfeito. Use laço para calcular os divisores.

n = int(input("TYPE A NUMBER: "))

#perfeito = True
divisores = []
for i in range(1,n):
    if n % i == 0:
        divisores.append(i)
    
print(divisores)
        
#ultimo = divisores.pop()
#print(divisores)
print(sum(divisores))
if sum(divisores) == n:
    print(f"{n} é um numero perfeito!")
else:
    print("Não é um numero perfeito!")