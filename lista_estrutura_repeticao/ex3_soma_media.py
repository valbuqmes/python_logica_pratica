#Leia um inteiro N e, em seguida, leia N números reais. Calcule e exiba: a soma total, a média aritmética, o
#maior e o menor valor lido. Valide que N seja maior que zero.


n = int(input("Digite um numero inteiro positivo:"))

while n <= 0 :
    n = int(input("Digite um numero inteiro positivo:"))

notas = []
soma = 0

for i in range(n):
    #adicionar valores em uma liasta, pega o nome da lista e coloca .append()
    notas.append(float(input(f"Digite a {i+1} nota: ")))
    while notas[i] < 0 or notas[i] > 10:
        notas[i] = int(input("Digite um valor entre 0 e 10: "))



maior = notas[0]
menor = notas[0]
#MAX e MIN
#maior = max(notas)
#menor = min(notas)

for nota in notas:
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

#soma = sum(notas)
for nota in notas:
    soma = soma + nota
tamanho = len(notas)
media = soma / tamanho
print(f"Notas: {notas} ")
print(f"Menor nota: {menor}")
print(f"Maior nota: {maior}")
print(f"Media do aluno: {media}")
