div = 2

numero = int(input("Type a number:"))
numero_divisores = 0

print("Numeros primos de 1 até ", numero,":")

if numero <=1:
    print(f"{numero} não é primo!")
elif numero == 2:
    print(f"{numero} é primo!")
elif numero % 2 == 0 and numero > 2:
    print(f"{numero} nao é primo!")






