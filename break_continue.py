contador = 0

while contador < 10:
    contador += 1
    print("Contador: ", contador)
    if contador == 5:
        continue
    if contador == 8:
        break
    #print("Contador: ", contador)