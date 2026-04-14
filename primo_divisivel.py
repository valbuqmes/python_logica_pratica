primo = True

num = int(input("Type a number:"))

div = 2

for div in range(div, num):
    if num % div == 0:
        primo = False
        print("Divisor: ", div)
       
if primo:
    print("O número é primo")
else:
    print("O número não é primo")