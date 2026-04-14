nota = int(input("Digite a nota: "))

while not (nota >= 0 and nota <= 10):
    print("Nota inválida. Digite uma nota entre 0 e 10.")
    nota = float(input("Digite a nota: "))

print("Nota válida: ", nota)