#Leia repetidamente notas de alunos (entre 0 e 10) até que o usuário digite -1 para encerrar. Para cada
#nota, informe se o aluno foi aprovado (nota >= 6) ou reprovado. Ao final, exiba: total de alunos, quantidade
#de aprovados, quantidade de reprovados e a média geral da turma.
alunos = []
#notas = []
aprovados = 0
reprovados = 0
soma = 0
qtd_alunos = 0

nota = float(input("Digite as notas\n Digite -1 para sair: "))

while nota != -1:

    if nota < 0 or nota > 10:
        print("Nota inálida!")
    else:
        alunos.append(nota)

    nota = float(input("Digite as notas dos alunos\n Digite -1 para sair: "))
    
print(alunos)

for aluno in alunos:
    nota = aluno
    soma += nota

    if nota >= 6:
        print("Aluno aprovado!")
        aprovados += 1
    else:
        print("Aluno reprovado!")
        reprovados += 1

qtd_alunos = len(alunos)

print(f"Total de alunos: {qtd_alunos}")
print(f"Quantidade de aprovados: {aprovados}")
print(f"Quantidade de reprovados: {reprovados}")
print("media da turma: ", soma /qtd_alunos)
