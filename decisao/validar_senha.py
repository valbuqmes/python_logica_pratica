senha = input("Digite sua senha: ")

contador = 0
# senha == senha.lower() se True, não há maisculo
# senha == senha.upper() se True, não ha caracteres maisculos



if len(senha) >= 10:
    contador += 1
    if senha != senha.lower():
        # Verifica se existe pelo menos uma letra MAIÚSCULA
        # senha.lower() transforma tudo em minúsculo
        # Se for diferente da original, tem maiúscula

        contador += 1

    if senha != senha.upper():
        # Verifica se existe pelo menos uma letra MINÚSCULA
        # senha.upper() transforma tudo em maiúsculo
        # Se for diferente da original, tem minúscula

        contador += 1
        
    if not senha.isalnum():
        # Verifica se existe pelo menos um CARACTERE ESPECIAL
        # isalnum() retorna True se tiver só letras e números
        # "not" inverte → aqui significa: tem algo além disso (ex: @, #, !)

        contador+=1

    #if not senha.isalpha():#verifica se há caracteres
        # Verifica se NÃO é apenas letras
        # Ou seja, garante que tenha pelo menos um número ou símbolo
      #   contador +=1

    if "123" in senha and "abc" in senha:
        contador -= 1

    if contador >= 4:
        print("Senha Forte")
    elif contador >= 3:
        print("Senha média")
    else:
        print("Senha Fraca")

else:

    print("SENHA INVALIDA!")
    

    



print(contador)
    