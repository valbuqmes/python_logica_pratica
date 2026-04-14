#Exercício 1 — Cadastro de Alunos

#Crie um programa que:

#Tenha um dicionário onde a chave é o nome do aluno e o valor é uma lista com 3 notas.

#O programa deve:
#Percorrer o dicionário usando for
#Calcular a média de cada aluno
#Mostrar:
#Nome do aluno
#Média
#Situação:
#"Aprovado" se média >= 7
#"Recuperação" se média >= 5 e < 7
#"Reprovado" se < 5

#dicionario gerado pelo gpt
alunos = {
    "João": [7.5, 8.0, 6.0],
    "Maria": [9.0, 5.5, 10.0],
    "Carlos": [4.0, 6.0, 5.0],
    "Ana": [10.0, 9.5, 8.5],
    "Pedro": [3.0, 4.5, 2.0]
}

for aluno in alunos:
    #print(aluno)
    notas = alunos[aluno]


    soma = 0

    #print(notas)
    #fazer com SUM
    #media = sum(notas)/len(notas)
    #print(media)
    #fazer sem o SUM
    for nota in notas:
        soma = soma / nota

    media = soma/len(notas)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"    

    print(aluno, media, situacao)