#Crie um programa para cadastrar funcionários. Cada funcionário tem: nome, sexo (M/F) e
#salário.
#O programa deve encerrar quando o usuário digitar 'fim' no campo nome.
#• Armazene cada funcionário como um dicionário dentro de uma lista.
##• Ao final, exiba a soma dos salários dos homens e a soma dos salários das mulheres.
#• Exiba também o total geral de salários e o número de funcionários cadastrados.

def ler_float(numero):
    while True:
        try:
            return float(input(numero))
        except ValueError:
            print("Digite um número válido.")


funcionarios = []#lista onde os dicionarios serão adicionados



sexo = ['M', 'F']          
opcoes = ['SIM', 'FIM']
opcao = input("Digite SIM para funcionar ? \n Digite FIM para encerrar!").upper()

while opcao != opcoes[0] and opcao != opcoes[1]:
    opcao = input("Digite SIM para funcionar? \n Digite FIM para encerrar!").upper()
    if opcao == 'FIM':
            break
  
   
salario_m = 0
salario_h = 0
total_salario = 0

while opcao != opcoes[1]:

    f = {}#dicinario que será adicionado na lista

    #for f in funcionarios:
    f['nome'] = input("Digite o nome do funcionario: ")
    f['sexo'] = input("Digite o sexo do funcionario M/F ").upper()

    while not f['sexo'] in sexo:
         f['sexo'] = input(" M/F ").upper()
         
    f['salario'] = ler_float("Digite um salario: ")

    funcionarios.append(f)#adicionando o dicionario na lista de funcionarios

    for i in funcionarios:
        if f['sexo'] == 'F':
            salario_m = salario_m + i['salario']
        elif f['sexo'] == 'M':
            salario_h = salario_h + i['salario']

        total_salario += i['salario']

    opcao = input("Digite SIM para funcionar ? \n Digite FIM para encerrar!").upper()
    while opcao != opcoes[0] and opcao != opcoes[1]:
        opcao = input("Digite SIM para funcionar? \n Digite FIM para encerrar!").upper()
        if opcao == 'FIM':
                break
       

for i in funcionarios:
    print('---------------------------------------------')
    print("| ",i," |")
    print('---------------------------------------------')

print('salario homens: ', salario_h)
print('salario muié: ', salario_m)
print("total salario: ", total_salario)


   ## for chave in funcionarios:
    #    funcionarios[chave] = input(f"Digite o {chave} do fncionario:")
     #   opcao = input("Deseja iniciar o programa? \n Digite FIM para encerrar!").upper()
      #  if opcao == 'fim':
       #     print(funcionarios)
        #    break


