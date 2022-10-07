infraction={
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100},
}

officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
}

db={}

pase5 = True
pase4 = True
pase3 = True
pase2 = True
pase = True
comprobante = True
while comprobante == True:

    print("***** Bienvenido al sistema de registro de multas *****")

    print("{Por favor, ingrese al numero que corresponda a la accion que quiere realizar \n 1: Ingresar un infractor \n 2: Eliminar un infractor \n 3: Consultar la lista de infraccciones \n 4: Salir")

    accion = input("Ingrese el numero aqui: ")

    if accion == str(1):

        while pase4 == True:

            nombrei = input("Por favor ingrese el primer nombre del infractor: ")

            apellidoi = input("Por favor ingrese el primer apellido del infractor: ")

            while pase2 == True:

                cedulai = input("Por favor ingrese el numero de cedula del infractor: ")


                if cedulai.isnumeric() == True:

                        pase2 = False

                elif cedulai.isnumeric() == False:

                    print("Por favor ingrese un caracter valido") 

                    

            print("Infracciones: \n 1: Choque \n 2: Semaforo \n 3: Falta de documentos")

            while pase == True:

                infraccion = input("Por favor escriba el numero de la infraccion que haya cometido el ciudadano/a: ")

                if infraccion == str(1) or infraccion == str(2) or infraccion == str(3):

                    pase = False

                else:

                    print("Por favor ingrese un caracter valido")

            print("Por favor seleccione el numero que corresponda al oficial de transito que coloco la multa: \n 1: Luis Bello 13452224 \n 2: Jose Quevedo 44235611 \n Antonio Guerra 12345678")



            while pase3 == True:

                oficial = input("Introduzca el numero aqui: ")


                if oficial == str(1) or oficial == str(2) or oficial == str(3):

                    pase3 = False


                else:

                    print("Por favor ingrese un caracter valido") 

            print(f"La informacion presentada a continuacion es correcta?\nNombre: {nombrei}\nApellido: {apellidoi}\nCedula de identidad: {cedulai}\nInfraccion: {infraction[int(infraccion)]}\nOficial: {officers[int(oficial)]}")

            while pase5 == True:

                aceptar = input("Coloque 'S' para Si o coloque 'N' para No")

                if aceptar.upper() == "S":

                    db[1] = [nombrei, apellidoi, cedulai, infraction[int(infraccion)], officers[int(oficial)]]

                    print(f"La nueva entrada de datos es: {db}")

                    aceptar2 = input("Desea hacer algo mas? \n Coloque 'S' para Si o coloque 'N' para No")

                    if aceptar2.upper() == "S":

                        pase5 = False
                        pase4 = False

                    elif aceptar2.upper() == "N":

                        pase5 = False
                        pase4 = False
                        comprobante = False
                        break

                        print("Gracias por usar el servicio")

                    else:

                        print("Por favor ingrese un caracter valido")


                    

                elif aceptar.upper() == "N":

                    pase5 = False

                else:

                    print("Por favor ingrese un caracter valido")



                



