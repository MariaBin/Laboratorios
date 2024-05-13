
X = 0
Y = 0

def MoverHaciaArriba():
    global Y
    Y += 1

def MoverHaciaAbajo():
    global Y
    Y -= 1

def MoverHaciaLaDerecha():
    global X
    X += 1

def MoverHaciaLaIzquierda():
    global X
    X -= 1

# Función para mostrar el menú y manejar las opciones
def mostrar_menu():
    print("Semana No. 12: Ejercicio 2")
    print("Coordenadas actuales del personaje:", X, ",", Y)
    print("Seleccione una opción:")
    print("a. Sube")
    print("b. Baja")
    print("c. Izquierda")
    print("d. Derecha")
    print("e. Salir")

# Función principal del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ").lower()

        if opcion == 'a':
            MoverHaciaArriba()
        elif opcion == 'b':
            MoverHaciaAbajo()
        elif opcion == 'c':
            MoverHaciaLaIzquierda()
        elif opcion == 'd':
            MoverHaciaLaDerecha()
        elif opcion == 'e':
            print("Coordenadas finales del personaje:", X, ",", Y)
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Llamada a la función principal
if __name__ == "__main__":
    main()
