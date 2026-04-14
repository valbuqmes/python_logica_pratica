#Sequência de Fibonacci
#Leia um inteiro N (maior ou igual a 1). Exiba os N primeiros termos da sequência de Fibonacci (0, 1, 1, 2, 3,
#5, 8...). Use a estrutura para.

n = int((input()))
primeiro = 0
segundo = 1

for i in range(n):
    print(primeiro)
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo

#print(primeiro)
#n = int((input()))
#primeiro = 0
#segundo = 1

#for i in range(n):
 #   print(primeiro)
  #  proximo = primeiro + segundo
   # primeiro = segundo
    #segundo = proximo
    #print(proximo)
