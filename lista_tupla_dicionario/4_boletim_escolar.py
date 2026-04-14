#Você recebeu os dados de vários alunos em uma lista de dicionários. Cada aluno possui:
#nome, AV1, AV2 e nota de recuperação.
#• Regras: Média do bimestre = (AV1 + AV2) / 2
#• Se média ≥ 6 → aprovado. Se média < 6 → usa recuperação:
#Média final = (média + recuperação) / 2 → ≥ 6: aprovado | < 6: reprovado
#• Exiba nome, média e situação de cada aluno.
#• Ao final, informe quantos foram aprovados e quantos reprovados.

alunos = []
media = 0
media_final = 0
qtd_aprovados = 0
qtd_reprovados = 0

opcoes = ['S', 'N']

s_n = input("Deseja iniciar o programa?\n [S/N] ").upper()

while s_n != opcoes[0] and s_n != opcoes[1]:
    s_n = input("Digite S para funcionar\n Digite N para encerrar! ").upper()
    if s_n == 'N':
            break



while s_n != 'N':
    a = {}
    
    a['nome'] = input("Digite o nome: ")
    a['av1'] = float(input("Digite av1: "))
    a['av2'] = float(input("Digite av2: "))
    a['rec'] = float(input("Digite a nota de recuperação: "))
    media = (a['av1'] + a['av2'])  / 2
    a['media'] = media

    alunos.append(a)

    for aluno in alunos:
        print('--------------------------------------')
        if aluno['media'] >=6 :
            print(f"{aluno['nome']} aprovado com a média {aluno['media']}")
            qtd_aprovados +=1
            a['situacao'] = "Aprovado"
        elif aluno['media'] < 6 :
            a['media_final']  = (aluno['media'] + aluno['rec']) / 2
            # qtd_reprovados += 1
           
            if a['media_final'] > 6:
                print(f"O Aluno {aluno['nome']} aprovado na recuperação!")
                qtd_aprovados += 1
                a['situacao'] = "Aprovado"
            else:
                print(f"O Aluno {aluno['nome']} reprovado")
                qtd_reprovados += 1
                a['situacao'] = "Reprovado"

    s_n = input("Deseja cadastrar mais alunos?\n [S/N]").upper()

    while s_n != opcoes[0] and s_n != opcoes[1]:
        s_n = input("Digite S para funcionar? \n Digite N para encerrar!").upper()
        if s_n == 'N':
                break

    

print("\n-------------------------------------------------------------------------")
print("Quantidade de alunos aprovados: ", qtd_aprovados)
print("Quantidade de alunos aprovados: ", qtd_reprovados)