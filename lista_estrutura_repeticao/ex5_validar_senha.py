#Validação de senha com tentativas limitadas
#Defina uma senha fixa no código (ex: 1234). Leia a tentativa do usuário. Enquanto a senha estiver errada e
#o número de tentativas for menor que 3, permita nova tentativa. Ao final, informe se o acesso foi liberado
#ou bloqueado e quantas tentativas foram usadas.
senha_definitiva = "ViniciusCarineLinkBowserNetero"
tentativa = 0
senha_digitada = input("Diga A senha: \n")
if senha_digitada == senha_definitiva:
        print("Senha validada, acesso liberado!")
else:
    tentativa += 1
    if tentativa == 3:
        print("Excedeu o numero de tentativas, Acesso bloqueado!")
    while tentativa < 3:
        senha_digitada = input("Tente outra vez: \n")
        tentativa += 1
