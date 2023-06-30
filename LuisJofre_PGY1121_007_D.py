from funciones_prueba import *
import numpy as np
import os
import time
import msvcrt
arreglo_jaulas = np.empty((2,5),object)
arreglo_jaulas.fill("🟩")
lista_rut = []
lista_nombre = []
lista_nom_Mascota = []
lista_identificador = []
lista_dias = []
lista_pisos = []
lista_jaulas = []
lista_precio_dia = []
precio_dia = 15000
while True:
    os.system('cls')
    print("""bien venido a Mascota segura
    menu de opciones
    1. grabar
    2. buscar
    3. retirarse
    4. salir""")
    while True:
        try:
            opc = int(input("ingrese opcion a ejecutar: "))
            if opc in (1,2,3,4):
                break
            else:
                print("opcin ingresada incorrecta, las opciones son 1,2,3,4")
        except:
            print("Error, debe ingresar un numero enero pocitivo")
    os.system('cls')
    if opc == 1:
        if "🟩" not in arreglo_jaulas:
            print("jaulas ocupadas en su totalidad, no se puede hacerpar ninguna mas")
            continue
        rut = validar_rut()
        nom = validar_nombre("su nombre")
        nom_mascota = validar_nombre("el nombre de su mascota")
        while True:
            try:
                print(f"precio por dia: ${precio_dia}")
                cant_dias = int(input("ingrese cantidad de dias que se queda su mascota: "))
                if cant_dias >=1:
                    break
                else:
                    print("debe ingresar por lo menos 1 dia")
            except:
                print("debe ingresar un numero entero pocitivo")
        lista_rut.append(rut)
        lista_nombre.append(nom)
        lista_nom_Mascota.append(nom_mascota)
        lista_dias.append(cant_dias)
        total = cant_dias * precio_dia
        lista_precio_dia.append(total)
        while True:
            os.system('cls')
            print("jaulas   1  2  3  4  5")
            for x in range(2):#filas
                print(f"piso {x+1} |", end=" ")
                for y in range(5):
                    print(arreglo_jaulas[x][y], end=" ")
                print()
            while True:
                try:
                    piso = int(input("ingrese piso para dejar a su mascota: "))
                    if piso in(1,2):
                        break
                    else:
                        print("piso ingresado incorrecto")
                except:
                    print("Error, debe ingresar un numero entero pocitivo")
            while True:
                try:
                    jaula = int(input("ingrese la jaula para dejar a su mascota: "))
                    if jaula in(1,2,3,4,5):
                        break
                    else:
                        print("jaula ingresada incorrecta")
                except:
                    print("Error, debe ingresar un numero entero pocitivo")
            if piso == 1:
                if jaula == 1:
                    lista_identificador.append(1)
                elif jaula ==2:
                    lista_identificador.append(2)
                elif jaula == 3:
                    lista_identificador.append(3)
                elif jaula == 4:
                    lista_identificador.append(4)
                else:
                    lista_identificador.append(5)
            else:
                if jaula == 1:
                    lista_identificador.append(6)
                elif jaula ==2:
                    lista_identificador.append(7)
                elif jaula == 3:
                    lista_identificador.append(8)
                elif jaula == 4:
                    lista_identificador.append(9)
                else:
                    lista_identificador.append(10)
            if arreglo_jaulas[piso-1][jaula-1] == "🟩":
                arreglo_jaulas[piso-1][jaula-1] = "🟥"
                lista_pisos.append(piso)
                lista_jaulas.append(jaula)
                print("jaula comprada con exito")
                print("precione una tecla para continuar")
                msvcrt.getch
                break
            else:
                print("jaula ocupada, elija otra")
    elif opc == 2:
        rut = validar_rut()
        if rut in lista_rut:
            pos = lista_rut.index(rut)
            print(f"""datos de la mascota {lista_nom_Mascota[pos]}
        piso: {lista_pisos[pos]}
        identificador: {lista_identificador[pos]}""")
            print("precione una tecla para continuar")
            msvcrt.getch()
        else:
            print("rut no registrado")
            time.sleep(2)
    elif opc == 3:
        rut = validar_rut()
        if rut in lista_rut:
            pos = lista_rut.index(rut)
            print(f"""boleta
        TOTAL A PAGAR: {lista_precio_dia[pos]}""")
        while True:
            confir = str(input("confirme monto a pagar(si o no): "))
            if confir.upper() in("SI","NO"):
                break
            else:
                print("dato ingresado erroneo, las opciones son SI o NO")
        if confir == "si":
            print("confirmando monto")
            time.sleep(2)
            print("tenga un buen dia")
            time.sleep(1)
            lista_rut.pop(pos)
            lista_nombre.pop(pos)
            lista_nom_Mascota.pop(pos)
            lista_identificador.pop(pos)
            lista_dias.pop(pos)
            lista_pisos.pop(pos)
            lista_jaulas.pop(pos)
            lista_precio_dia.pop(pos)
        else:
            print("volviendo al menu principal....")
            pass
    else:
        print("cerrando programa, tenga un buuen dia...")
        time.sleep(2)
        exit()