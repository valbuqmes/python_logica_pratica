funcionarios = [ ]
qtd_funcionarios = int(input("Digite quantos funcionarios deseja inserir: "))

#lista de dicionario para varios funcionarios
for i in range(qtd_funcionarios):

    #declaracao dos dicionarios
    funcionario = {}

    #adicionar chave valor ao dicionario
    funcionario["nome"] = input("Nome: ")
    funcionario["sexo"] = input("Sexo: ")
    funcionario["salario"] = float(input("Salário: "))
    print(funcionario)
    funcionarios.append(funcionario)
    print(funcionarios)


