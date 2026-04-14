#dicionario  { }
#dicionarios são coleçoes desodarnadas de pares de chave-valor, cada chave é única
#.keys retorna as chaves
#.values retorna os valores

pessoa = {"nome": "Carine", "idade": 24, "Cidade":"Manaus"}

#precisa do list porque python retorna objeto
valores = list(pessoa.values())
print(valores)
chaves = list(pessoa.keys())
print(valores)
print(pessoa)

#transforma em tupla
items = list(pessoa.items())
print(items)
#acessar valores
#acessa o segundo(1) elemento e o segundo indice dentro do elemento
#print(items[1][1])

print(pessoa.get("estado"))
print(pessoa.get("idade"))


#imprimir direto sem salvar em variavel
#print(pessoa.keys())
#print(pessoa.values())
