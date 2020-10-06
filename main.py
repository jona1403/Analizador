from Lectura_de_Archivos import Lectura
from Graficar_Mapa import Grafica_Mapa
from Graficar_Ruta import Filtro_Rutas
import os
Lista_Rutas = []
Lista_Estaciones = []
Nombre_Mapa = ""
Estacion_Inicio = ""
Estacion_Fin = ""
while True:
    print("-------------------------------------------------------")
    print("Lenguajes Formales y de Programación(796), Sección A-")
    print("Jonathan Alexander Alvarado Fernández, carné: 201903004")
    print("-------------------------------------------------------")
    print("1. Cargar Archivo")
    print("2. Graficar Ruta")
    print("3. Graficar Mapa")
    print("4. Salir")
    print("-------------------------------------------------------\n")
    opcion = input("Ingrese la opción deseada: ")
    if opcion == "1":
        Ruta = input("Ingrese la ruta del archivo: ")
        if os.path.isfile(Ruta) and Ruta[-4:] == ".txt":
            Lista_Rutas, Lista_Estaciones, Nombre_Mapa = Lectura(Ruta)
        else:
            print("El documento no existe o no es .txt")
        input()
    elif opcion == "2":
        if Lista_Rutas != [] and Lista_Estaciones != []:
            Estacion_Inicio = input("Ingrese la estación inicial: ")
            Estacion_Fin = input("Ingrese la estación final: ")
            Filtro_Rutas(Estacion_Inicio, Estacion_Fin, Lista_Estaciones, Lista_Rutas)
        input()
    elif opcion == "3":
        if Lista_Rutas != [] and Lista_Estaciones != [] and Nombre_Mapa != "":
            Grafica_Mapa(Lista_Rutas, Lista_Estaciones, Nombre_Mapa)
            print("Gráfica de mapa generada existosamente :)")
        else:
            print("Datos faltantes")
        input()
    elif opcion == "4":
        break
    else:
        print("Opción invalida, vuelva a intentarlo")