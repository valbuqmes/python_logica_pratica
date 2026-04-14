#Leia um inteiro N (maior ou igual a zero). Calcule o fatorial de N usando a estrutura repita...enquanto.
#Exiba o resultado. Lembre que 0! = 1.

n = int(input("Digite um numero maior ou igual a 0: "))

while n < 0:
    n = int(input("Digite um numero maior ou igual a 0: "))
fatorial = 1

for i in range(1, n +1):
    fatorial = fatorial * i
print(f"Fatorial de {n} é {fatorial}")

