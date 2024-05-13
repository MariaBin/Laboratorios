# Semana No. 10: Ejercicio 1
print("Semana No. 10: Ejercicio 1")
numero_mes = int(input("Ingrese el número del mes: "))
if numero_mes < 1 or numero_mes > 12:
    print("Error: El número a ingresar debe estar contenido entre 1 y 12")
else:
    if numero_mes == 1:
        nombre_mes = "Enero"
    elif numero_mes == 2:
        nombre_mes = "Febrero"
    elif numero_mes == 3:
        nombre_mes = "Marzo"
    elif numero_mes == 4:
        nombre_mes = "Abril"
    elif numero_mes == 5:
        nombre_mes = "Mayo"
    elif numero_mes == 6:
        nombre_mes = "Junio"
    elif numero_mes == 7:
        nombre_mes = "Julio"
    elif numero_mes == 8:
        nombre_mes = "Agosto"
    elif numero_mes == 9:
        nombre_mes = "Septiembre"
    elif numero_mes == 10:
        nombre_mes = "Octubre"
    elif numero_mes == 11:
        nombre_mes = "Noviembre"
    elif numero_mes == 12:
        nombre_mes = "Diciembre"
    print("MES: " + nombre_mes)

# Semana No. 10: Ejercicio 2
print("Semana No. 10: Ejercicio 2")

numero1 = int(input("Ingrese el primer número entero mayor a cero: "))
while numero1 <= 0:
    print("Error: El número debe ser mayor a cero")
    numero1 = int(input("Ingrese el primer número entero mayor a cero: "))

numero2 = int(input("Ingrese el segundo número entero mayor a cero: "))
while numero2 <= 0:
    print("Error: El número debe ser mayor a cero")
    numero2 = int(input("Ingrese el segundo número entero mayor a cero: "))

numero3 = int(input("Ingrese el tercer número entero mayor a cero: "))
while numero3 <= 0:
    print("Error: El número debe ser mayor a cero")
    numero3 = int(input("Ingrese el tercer número entero mayor a cero: "))