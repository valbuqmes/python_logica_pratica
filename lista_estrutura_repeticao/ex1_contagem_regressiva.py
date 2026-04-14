#01 Contagem regressiva com enquanto
#Leia um número inteiro positivo N. Usando a estrutura enquanto, imprima uma contagem regressiva de N
#até 1 e, ao final, exiba a mensagem "Fim!".


n = int(input("Digite um numero inteiro positivo: "))

while n <= 0:
    n = int(input("Digite um numero inteiro positivo: "))

print(n)
while n != 1:

    n = n - 1
    print(n)
    if n == 1:
        print("FIM!")