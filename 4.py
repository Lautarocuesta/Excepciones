def matematica(a, b):
    try:
        
     resultado = a + b
     print("El resultado de la operación es:", resultado)

    except TypeError:
       print("Error: Los argumentos deben ser del tipo de datos numéricos.")

    finally:
        print("Gracias por usar la función.")

# Ejemplo de uso 
matematica(5, 3)  # funciona correctamente
matematica("Hola", 3)  # funciona incorrectamente
