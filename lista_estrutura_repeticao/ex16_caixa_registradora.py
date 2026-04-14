#Simule uma caixa registradora: enquanto o usuário não digitar 0, leia o preço de um produto. Acumule o
#total. A cada item, informe o subtotal parcial. Ao encerrar, aplique desconto de 10% se o total ultrapassar
#R$ 100. Exiba o total bruto, desconto e total final.

subtotal_parcial = 0
preco = float(input("Type a value: "))
while preco != 0:
    subtotal_parcial = subtotal_parcial + preco
    print("Subtotal parcial: ",subtotal_parcial)
    preco = float(input("Type a value: "))


if subtotal_parcial > 100:
    desconto = subtotal_parcial * 0.10
else:
    desconto = 0

total_final = subtotal_parcial - desconto

print("Total Bruto: ", subtotal_parcial)
print("Desconto: ", round(desconto, 2))
print("Total final: ", total_final)
