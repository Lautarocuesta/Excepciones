
def indice():
    try:
        
        lista = [1,2,3]

        # acceder a un elemento en una posición específica
        elemento = lista[0]

        # Imprimir el elemento
        print("El elemento en la posición 0 es:", elemento)

    except IndexError:
       print("Error: No hay elementos en la lista o se está intentando acceder a un índice fuera del rango.")

    finally:
        # Código que se ejecuta siempre, independientemente de si se producen excepciones o no
        print("Gracias por usar el programa.")

if __name__ == "__main__":
    indice()