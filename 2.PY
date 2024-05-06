def entero():
    try:
        # Solicitar al usuario ingresar un número
        str = input("Ingrese un número: ")
        numentero = int(str)

        # Imprimir el número entero
        print("El número ingresado es:", numentero)

    except ValueError:
       print("Error: Por favor ingrese un valor numérico válido.")

    finally:
       print("Gracias por usar el programa.")

if __name__ == "__main__":
    entero()