
#validar rut
def validar_rut():
    while True:
        try:
            rut = int(input("ingrese rut sin dijito verificador y sin puntuacion: "))
            if rut >= 1000000 and rut <=99999999:
                return
            else:
                print("rut ingresado erroneo")
        except:
            print("Error, debe ingresar un rut entero pocitivo")
#validar nombre
def validar_nombre(nombre: str):
    while True:
        nom = input(f"ingrese {nombre}: ")
        if len(nom.strip())>= 3 and nom.isalpha():
            return
        else:
            print("debe ingresar un nombre de 3 letras como minimo")