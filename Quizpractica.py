numero = input("Por favor ingresa un numero para ser evaluado: ")

numero = int(numero)
total = 0

for i in range(1, numero):
    
    if numero % i == 0:
        total += i

    else:
        total += 0

if numero == total:

    print("El numero ingresado es prefecto")

else:
    print("EL n[umero ingresado no es perfecto")

