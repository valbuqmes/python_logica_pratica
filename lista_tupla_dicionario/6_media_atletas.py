#Em uma competição de salto em distância, cada atleta tem direito a cinco saltos.
#O resultado final é a média dos cinco valores.
#• Leia o nome do atleta com input(). Se não digitar nome, o programa encerra.
#• Para cada atleta, leia os cinco valores de salto e armazene em uma lista.
#• Exiba o nome, os saltos e a média calculada.
#• O programa deve aceitar múltiplos atletas até que nome vazio seja informado.


atletas = []

while True:
    a = {}
    
  
    a['nome'] = input("Digite o nome do atleta: ").strip()
    if not a['nome']:#como string é valor verdadeiro e string vazia é falso, se for falso nem entra no looping mas agora, com o not, foi negado então se a string estiver vazia executa esse bloco e finaliza o codigo
             break
     
    a['primeiro_salto'] = float(input("Digite a distancia do primeiro salto: "))
    a['segundo_salto']  = float(input("Digite a distancia do segundo salto: "))
    a['terceiro_salto'] = float(input("Digite a distancia do terceiro salto: "))
    a['quarto_salto'] = float(input("Digite a distancia do quarto salto: "))
    a['quinto_salto'] = float(input("Digite a distancia do quinto salto: "))
    a['media'] = (a['primeiro_salto'] + a['segundo_salto'] + a['terceiro_salto'] + a['quarto_salto'] + a['quinto_salto']) / 5

    atletas.append(a)

print("Programa encerrado!")
print(atletas)

    
