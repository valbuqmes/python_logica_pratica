x = int(input("Digite um numero: "))

soma  = 0

for i, j  in enumerate(range(1,(x*2)+1,2),1):
    print(f"{i}/{j}")
    soma = soma + (1/ i)
    #print(soma)

print(soma)