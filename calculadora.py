print("""

Seleccione qué operación quiere hacer (solo el número):
      1 suma.
      2 resta.
      3 multiplicación.
      4 división.

""")

seleccion = 0
while seleccion not in [1, 2, 3, 4]:
    try:
        seleccion = int(input("Ingrese el número de la operación deseada: "))
        if seleccion not in [1, 2, 3, 4]:
            print("Por favor, ingrese un número válido (1, 2, 3 o 4).")
    except ValueError:
        print("Por favor, ingrese un número válido (1, 2, 3 o 4).")

if seleccion == 1: 
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    except ValueError:
        print("Por favor, ingrese números válidos.")
elif seleccion == 2: 
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    except ValueError:
        print("Por favor, ingrese números válidos.")
