list_numeros = [1,2,3,4,5,6,7,8,9,10]

par, impar = 0, 0

for numero in list_numeros:
    if numero % 2 == 0:
        par = par +  numero
    if numero % 2 != 0:
        impar +=  numero
    
print("Soma par: ", par)
print("Soma ímpar: ", impar)

