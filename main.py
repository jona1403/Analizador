from Lectura_de_Archivos import Lectura
from Graficar_Mapa import Grafica_Mapa
Lista_Rutas = []
Lista_Estaciones = []
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
        Lista_Rutas, Lista_Estaciones = Lectura(Ruta)
        input()
    elif opcion == "2":
        print("Graficando Ruta....................")
        input()
    elif opcion == "3":
        Grafica_Mapa(Lista_Rutas, Lista_Estaciones)
        input()
    elif opcion == "4":
        break
    else:
        print("Opción invalida, vuelva a intentarlo")