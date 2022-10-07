comprobar = True


while comprobar == True:


    numero = input("Por favor ingrese un numero natural: ")

    numeroprimo = numero.isnumeric()
    

    if numeroprimo == True:

        print("Perfecto")

        comprobar = False
    else:

        print("Error, por favor ingresa un numero natural")


npdefernat = (2**(2**int(numero))) + 1

cprimo = 0


for i in range(1, npdefernat + 1):


    if npdefernat % i == 0:

        cprimo += 1
    
    else:

        cprimo += 0


if cprimo == 2:
    
    print("El numero seleccionado es un numero primo de fernat")

elif cprimo > 2:

    print("El numero seleccionado no es un numero primo de fernat")




