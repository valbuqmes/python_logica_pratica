def saudacoes(nome= "Mundo"):
    return f"Olá {nome}"


print(saudacoes())
print(saudacoes("Ana"))

def soma(a=2, b=2):
    return a + b

print(soma())
print(soma(5,8))


#raise ValueError("Valores negativos não são permitidos") // quebra o código

