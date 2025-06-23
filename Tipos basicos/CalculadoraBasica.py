# Calculadora básica en Python

print("CALCULADORA BÁSICA")

operacion = input("¿Qué operación querés realizar? (suma, resta, multiplicar, dividir): ").lower()

try:
    n1 = float(input("Ingresá un número: "))
    n2 = float(input("Ingresá otro número: "))

    if operacion == "suma":
        resultado = n1 + n2
        print(f"El resultado es: {resultado}")

    elif operacion == "resta":
        resultado = n1 - n2
        print(f"El resultado es: {resultado}")

    elif operacion == "multiplicar":
        resultado = n1 * n2
        print(f"El resultado es: {resultado}")

    elif operacion == "dividir":
        if n2 == 0:
            print("ERROR: No se puede dividir por 0")
        else:
            resultado = n1 / n2  # Si querés solo enteros, cambiá a //
            print(f"El resultado es: {resultado}")

    else:
        print("Opción incorrecta")

except ValueError:
    print("ERROR: Ingresaste un valor no numérico.")
