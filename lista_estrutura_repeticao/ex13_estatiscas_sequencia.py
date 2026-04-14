#Leia números reais até que o usuário digite 0. Ao final, exiba: quantidade de números digitados, soma,
#média, maior valor, menor valor, quantidade de números positivos e quantidade de negativos. Trate o caso
#em que nenhum número foi digitado.

numeros_digitados = []
numero_reais = float(input("Digite um numero: ")) 
qtd_numeros_positivos = 0
qtd_numeros_negativs = 0

while numero_reais != 0:
    numeros_digitados.append(numero_reais)
    print(numeros_digitados)

    
    if numero_reais < 0:
        qtd_numeros_negativs += 1
    elif numero_reais > 0:
        qtd_numeros_positivos += 1



    numero_reais = float(input("Digite um numero: ")) 

if len(numeros_digitados) == 0:
    print("Nenhum numero foi digiatado!")
else:

    print("Quantidade de numeros digitados: ", len(numeros_digitados))
    print("Soma dos numeros: ", sum(numeros_digitados))
    print("Media dos numeros", sum(numeros_digitados)/len(numeros_digitados))
    print("Quantidade de numeros positivos: ", qtd_numeros_positivos)
    print("Quantidade de numeros negativos: ", qtd_numeros_negativs)
    print("Maior valor: ", max(numeros_digitados))
    print("Menor valor: ", min(numeros_digitados))



