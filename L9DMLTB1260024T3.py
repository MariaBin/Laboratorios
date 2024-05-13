def convertir_metros(metros):
    millimetros = metros * 1000
    centimetros = metros * 100
    kilogrametros = metros * 0.001
    pies = metros * 3.28084
    pulgadas = pies * 12

    print(f"{metros} metros es equivalente a:")
    print(f"{millimetros:.1f} milímetros")
    print(f"{centimetros:.1f} centímetros")
    print(f"{kilogrametros:.6f} kilómetros")
    print(f"{pies:.3f} pies")
    print(f"{pulgadas:.3f} pulgadas")

metros = float(input("Ingrese una cantidad de metros: "))
convertir_metros(metros) 