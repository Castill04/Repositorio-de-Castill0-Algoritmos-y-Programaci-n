

comprobar = True

while comprobar == True:

    n = int(input("ingrese un numero entero positivo: "))

    if n > 0:

        

        for i in range(1, 11):
            print(n, "por", i, "es igual a", n*i)

        comprobar = False
            

    else:
        print("El numero ingresado es incorrecto, intentelo de nuevo")

