def division():
    try:
        # Ingresar al usuario algun numero
        numerador = float(input("Ingrese el numerador: "))
        denominador = float(input("Ingrese el denominador: "))
        resultado = numerador / denominador

        # Imprimir el resultado
        print("El resultado de la división es:", resultado)

    except ZeroDivisionError:
         print("Error: No se puede dividir entre cero. Intente con otro denominador.")
   
    finally:
        print("Gracias por usar el programa.")

if __name__ == "__main__":
    division()