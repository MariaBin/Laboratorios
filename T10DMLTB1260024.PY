
print("Nombre: Daisy María Letizia Tzul Bin")
print("Carné: 1260024")


dia = int(input("Ingrese el día de nacimiento (1-31): "))
mes = int(input("Ingrese el mes de nacimiento (1-12): "))
año = int(input("Ingrese el año de nacimiento (1900-2021): "))


ar_start = (3, 21)
ta_start = (4, 20)
ge_start = (5, 21)
ca_start = (6, 21)
le_start = (7, 23)
vi_start = (8, 23)
li_start = (9, 23)
es_start = (10, 23)
sc_start = (11, 22)
sa_start = (12, 21)
ca_end = (12, 31)


if año < 1900 or año > 2021:
    print("Año de nacimiento no válido")
elif mes < 1 or mes > 12:
    print("Mes de nacimiento no válido")
elif dia < 1 or dia > 31:
    print("Día de nacimiento no válido")
elif mes == 3 and dia >= 21:
    print("Su signo zodiacal es: Aries")
elif mes == 4 and dia <= 20:
    print("Su signo zodiacal es: Aries")
elif mes == 4 and dia >= 21:
    print("Su signo zodiacal es: Tauro")
elif mes == 5 and dia <= 20:
    print("Su signo zodiacal es: Tauro")
elif mes == 5 and dia >= 21:
    print("Su signo zodiacal es: Géminis")
elif mes == 6 and dia <= 20:
    print("Su signo zodiacal es: Géminis")
elif mes == 6 and dia >= 21:
    print("Su signo zodiacal es: Cáncer")
elif mes == 7 and dia <= 22:
    print("Su signo zodiacal es: Cáncer")
elif mes == 7 and dia >= 23:
    print("Su signo zodiacal es: Leo")
elif mes == 8 and dia <= 22:
    print("Su signo zodiacal es: Leo")
elif mes == 8 and dia >= 23:
    print("Su signo zodiacal es: Virgo")
elif mes == 9 and dia <= 22:
    print("Su signo zodiacal es: Virgo")
elif mes == 9 and dia >= 23:
    print("Su signo zodiacal es: Libra")
elif mes == 10 and dia <= 22:
    print("Su signo zodiacal es: Libra")
elif mes == 10 and dia >= 23:
    print("Su signo zodiacal es: Escorpio")
elif mes == 11 and dia <= 21:
    print("Su signo zodiacal es: Escorpio")
elif mes == 11 and dia >= 22:
    print("Su signo zodiacal es: Sagitario")
elif mes == 12 and dia <= 21:
    print("Su signo zodiacal es: Sagitario")
elif mes == 12 and dia >= 22:
    print("Su signo zodiacal es: Capricornio")
else:
    print("Su signo zodiacal es: Capricornio")