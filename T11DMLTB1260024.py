#Daisy María Tzul Bin; Carné: 1260024
print("Semana 11 Ejercicio 1")
n=int(input("Ingrese un numero mayor a 0\n"))
#Definicion de variables
a=0
b=1
c=0
i=2
resultado=""
if (n<=0):
    print ("Error, debe ser mayor a 0")
else:
  resultado=str(a)
  if n>1: resultado +=", "+str(b)
while i<n:
 c=a+b
 resultado +="," + str(c)
 a=b
 b=c
 i=i+1
 if n==1:
  break
 print (resultado)
else:
 print (resultado)