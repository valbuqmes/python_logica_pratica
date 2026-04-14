alunos = {
    "Ana": {"av1": 7.0, "av2": 5.0, "rec": 6.0},
    "Carlos": {"av1": 4.0, "av2": 3.5, "rec": 7.0},
    "Marina": {"av1": 8.0, "av2": 9.0, "rec": 0},
    "João": {"av1": 5.5, "av2": 6.0, "rec": 5.0}
}

#for i in alunos:
  #  print(i)

#itens = alunos.items()
#print(itens)

#ana = alunos["Ana"]
#carlos = alunos["Carlos"]
#marina = alunos["Marina"]
#joao = alunos["João"]

#print(ana)
#print(carlos)
#print(marina)
#print(joao)
media_final = 0
#items retorna uma tupla, por isso acesso nome(chave) e notas(valor) dentro de alunos
#exemplo:
#nome = "Ana"
#notas = {"av1": 7.0, "av2": 5.0, "rec": 6.0}
aprovados = 0
reprovados = 0
for nome, notas in alunos.items():
   # print("Dentro de cada nome: ", nome)
   # print("valores dentro de nomes: ",notas)
    media = (notas["av1"] + notas["av2"]) / 2
    #print(notas["av1"])
    #print(notas)
    print(nome, media)

    if media >= 6:
       print(f"Aluno : {nome} Aprovado com a media: {media}")
    else:
        media_final = (media + notas["rec"]) / 2
        print("Media final :", media_final)
        if media_final >= 6:
            print("Aluno Aprovado!")
        else:
            print("Aluno reprovado!")



