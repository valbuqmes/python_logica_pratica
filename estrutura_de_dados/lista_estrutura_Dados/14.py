lista_perguntas = ["Telefonou para a vitima?", "Esteve no local do crime", "Mora perto da vitima?", "Devia para a vitma", "Ja tranalhou com a vitima?"]
contador = 0

print("Responda com S ou N\n")

#resposta = 'S'
qtd_respostas = 0
respostas = []

#percorre a lista de perguntas
for pergunta in lista_perguntas:
    print(pergunta)
    #resposta = input("")
    
    #recepe as respostas e coloca em caixa alta com o upper()
    resposta_pergunta = input("RESPONDA: ").upper()

    #validacao
    while resposta_pergunta != 'S' and resposta_pergunta != 'N':
        print("RESPOSTA INVALIDA!")
        resposta_pergunta = input("RESPONDA:").upper()
    
    #adiciona as respostas na lista respostas
    respostas.append(resposta_pergunta)
    
    print(respostas)
    #conta quantos caracteres S tem na lista
    qtd_respostas = respostas.count('S')
    print(qtd_respostas)
    

    #if resposta == 'S' or resposta == 's':
    #    contador +=1


if qtd_respostas > 4:
    print("Assassino!")
elif qtd_respostas >= 3 and qtd_respostas <= 4:
    print("Cumplice!")
elif qtd_respostas == 2:
    print("Suspeito")
else: 
    print("Inocente")