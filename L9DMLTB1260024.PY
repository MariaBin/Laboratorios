#Laboratoriosemana9
print ("Ejercicio 1: Operaciones Aritméticas ")
numero1= int(input("Ingrese el primer número: "))
numero2= int(input("Ingrese el segundo número: "))
total=numero1+numero2
diferencia=numero1-numero2
producto=numero1*numero2
divreal=numero1/numero2
divent=numero2//numero2
residuo=numero1%numero2
potencia=numero1**numero2
print("suma", total)
print("resta "+str(diferencia))
print("multiplicación ",producto)
print("División real ", divreal)
print("División entera ", divent)
print("División modular: ", residuo)
print("potencia", potencia)
print(numero1,"^", numero2,"=",potencia)
print()
print("Ejercicio2: Operaciones Booleanas ")
igualdad=numero1==numero2
mayorque=numero1>numero2
menorque=numero1<numero2
distinto=numero1!=numero2
print(numero1, "es igual a ",numero2, ":", igualdad)
print(numero1, "es mayor que ",numero2, ":", mayorque)
print(numero1, "es menor que ",numero2, ":", menorque)
print(numero1, "es distinto ",numero2, ":", distinto)
print()
print("Ejercicio 3: Jerarquia de operadores ")
a=int(input("Ingrese el primer valor: "))
b=int(input("Ingrese el segundo valor: "))
c=int(input("Ingrese el tercer valor: "))
i=a*b+c
ii=a*(b/c)
iii=a/(b+c)
iv=((3*a)+(2*b))/(c**2)
print("a*")