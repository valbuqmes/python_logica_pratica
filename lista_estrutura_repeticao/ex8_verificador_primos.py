#Leia um inteiro N maior que 1. Verifique se N é primo: um número é primo se for divisível apenas por 1 e
#por ele mesmo. Use laço para testar os divisores. Exiba "primo" ou "nao primo".

numero_divisores = 0
numero = int(input("Digite um numero para verificar se ele é primo: "))

#metade = int(numero // 2)

for numeros in range(1, numero // 2 + 1):
    print(numeros)
    if numero % numeros == 0:
        numero_divisores += 1
       

if numero_divisores > 2:
    print(f"{numero} não é primo! ")
else:
    print(f"{numero} é primo! ")