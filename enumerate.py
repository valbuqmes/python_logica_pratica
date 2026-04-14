
frutas = ["Maçã", "Banana", "Cereja", "Laranja"]

for i, valor in enumerate(frutas, start = 0):
     print(f"Índice: {i} - Valor: {valor}")

print("-------------------------------")

for i in range(len(frutas)):
    print(f"Índice: {i} - Valor: {frutas[i]}")