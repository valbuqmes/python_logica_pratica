#Leia um número inteiro N (entre 1 e 10). Exiba a tabuada completa de N (de 1 a 10) no formato: N x i =
#resultado. Use a estrutura para.

numero = int(input("Digite um numero entre 1 e 10: "))
while numero < 1 or numero > 10:
    numero = int(input("DIgite um numero entre 1  e 10: "))

#com RANGE
for i in range(1, 11):
    tabuada = numero * i
    print(f"{numero} x {i} = {tabuada}")


