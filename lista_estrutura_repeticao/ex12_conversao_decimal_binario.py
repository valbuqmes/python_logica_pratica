#Leia um inteiro positivo N. Converta-o para binário sem usar funções prontas: use laço enquanto dividindo
#N por 2 e acumulando os restos. Exiba o número binário correspondente.

numero_inteiro_positivo = int(input("Digite um numero inteiro psoitivo: "))
restos = []

while numero_inteiro_positivo > 0:
    resto = numero_inteiro_positivo % 2 #pega o resto da divisao
    restos.append(resto)
    numero_inteiro_positivo = numero_inteiro_positivo // 2 #divide por 2 para continuar o loop
    
print(restos[::-1])
