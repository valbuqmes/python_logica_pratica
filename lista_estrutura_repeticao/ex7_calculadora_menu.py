#Calculadora com menu repetido
#Exiba um menu com as opções: 1-Somar, 2-Subtrair, 3-Multiplicar, 4-Dividir, 0-Sair. Enquanto o usuário
#não escolher 0, leia dois números, execute a operação escolhida e exiba o resultado. Trate a divisão por
#zero. Ao sair, exiba quantas operações foram realizadas.

contador = 0
print("|| 1-Somar || 2-Subtrair || 3-Multiplicar || 4-Dividir || 0-Sair || \n")

escolha = float(input("Qual a sua escolha: \n"))

while escolha > 4 or escolha < 0:
    escolha = int(input("Valor invalido, tente outra vez! \n || 1-Somar || 2-Subtrair || 3-Multiplicar || 4-Dividir || 0-Sair || :"))


while escolha in [1,2,3,4]:

    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite outro numero: "))

    if escolha == 1:
        print(f"{n1} + {n2} = {n1 + n2}\n")
        contador += 1
    elif escolha == 2:
        print(f"{n1} - {n2} = {n1 - n2}\n")
        contador = contador + 1
    elif escolha == 3:
        print(f"{n1} * {n2} = {n1 * n2}\n")
        contador += 1

    else:
        if n2 == 0:
            print("Impossivel dividir por 0")
        else:
            print(f"{n1} / {n2} = {n1 / n2}\n")
            contador += 1



    print("|| 1-Somar || 2-Subtrair || 3-Multiplicar || 4-Dividir || 0-Sair || \n")
    escolha = int(input("Qual a sua escolha: \n"))

    while escolha > 4 or escolha < 0:
        escolha = int(input("Valor invalido, tente outra vez: \n || 1-Somar || 2-Subtrair || 3-Multiplicar || 4-Dividir || 0-Sair || "))

if escolha == 0:
    print(f"Operações realizadas: {contador}")
