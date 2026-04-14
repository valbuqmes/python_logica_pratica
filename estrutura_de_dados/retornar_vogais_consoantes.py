vogais = ["a","e","i", "o", "u"]

contador_de_vogais = 0
contador_de_consoantes = 0

entrada = input("Digite uma palavra: \n").lower()

for letra in entrada:

    if letra.isalpha():

        if letra in vogais:

            contador_de_vogais += 1

        if letra not in vogais:
            
            contador_de_consoantes +=1

        

print(f"Vogais: ", contador_de_vogais)
print(f"Consoantes: ", contador_de_consoantes)