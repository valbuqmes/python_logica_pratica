#Defina um número secreto fixo no código (ex: 42). O usuário tem até 5 tentativas para adivinhar. A cada
#tentativa errada, informe se o chute foi "muito baixo" ou "muito alto". Se acertar, parabenize e informe em
#quantas tentativas. Se esgotar as tentativas, revele o número secreto.

numer_secreto = 42

tentativas = 0

while tentativas < 5:
    palpite = int(input("Palpite: "))

    if palpite == numer_secreto:
        print(f"VOCE ACERTOU!\n PARABÉNS\n Tentativas: {tentativas}")

    elif palpite <= (numer_secreto // 2 ):
        print("MUITO BAIXO")
    elif palpite < numer_secreto:
        print("QUASE! CHUTE MAIS ALTO")
    else:
        print("MUITO ALTO, CHUTE MAIS BAIXO!")
    
    
    tentativas += 1

if tentativas == 5:
        print(f"Tentativas esgotadas! \n {numer_secreto} era o numero secreto!")