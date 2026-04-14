linhas = int(input("Digite um numero: "))

for i in range(1, linhas+1):#numero de linhas
    print(" " * (linhas - i) + "*" *(2*i-1) )#multiplica os espaços vazios por n-1, ou seja, o numero de repetições, coloca os espaços antes dos asteriscos