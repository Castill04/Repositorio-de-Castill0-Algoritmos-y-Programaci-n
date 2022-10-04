comprobar = True

while comprobar == True:

    n = input("Ingrese un numero entero positivo o, en caso de querer cerrar el programa, escribir 'terminar'")

    if n.upper() == "TERMINAR" :

        comprobar = False

        print("Gracias por usar el servicio :)")

    if n > 0:

        n = int(n)

        resultado = 0
        
        for i in range(1,n+1):

            resultado += (1/i) 
        
        print("El resultado es: ", resultado)

    else:
        print("El valor que usted ingreso no puede ser proicesado, por favor intentelo de nuevo")

