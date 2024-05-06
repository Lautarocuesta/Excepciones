# Excepciones
EJER 1: 
# Programa de División con Manejo de Excepciones
## Uso

1. Ejecuta el programa.
2. Ingresa el numerador y el denominador cuando se te solicite.
3. El programa calculará la división y mostrará el resultado si no hay errores.
4. Si el denominador es cero, se mostrará un mensaje de error y se pedirá al usuario que ingrese otro denominador.
5. Si el usuario ingresa un valor no válido (por ejemplo, una letra en lugar de un número), se mostrará un mensaje de error.

## Manejo de Excepciones

El programa maneja las siguientes excepciones:

- **ZeroDivisionError:** Si el denominador es cero, se muestra un mensaje de error y se pide al usuario que ingrese otro denominador.

El bloque `finally` se utiliza para imprimir un mensaje de agradecimiento que se ejecutará siempre, independientemente de si se producen excepciones o no.

EJER 2:
# Programa de Conversión a Entero con Manejo de Excepciones
## Uso

1. Ejecuta el programa.
2. Ingresa un número cuando se te solicite.
3. El programa intentará convertir el número ingresado a un entero.
4. Si el usuario ingresa un valor no válido (por ejemplo, una letra en lugar de un número), se mostrará un mensaje de error.
5. Si el número ingresado es válido, se imprimirá el número entero.

## Manejo de Excepciones

El programa maneja la siguiente excepción:

- **ValueError:** Si el usuario no ingresa un valor numérico válido (por ejemplo, una letra en lugar de un número), se muestra un mensaje de error indicando que se debe ingresar un valor numérico válido.

El bloque `finally` se utiliza para imprimir un mensaje de agradecimiento que se ejecutará siempre, independientemente de si se producen excepciones o no.

EJER 3:
# Programa de Acceso a Índice con Manejo de Excepciones

## Uso

1. Ejecuta el programa.
2. El programa intentará acceder al primer elemento en la posición 0 de la lista.
3. Si la lista está vacía o si se intenta acceder a un índice fuera del rango de la lista, se mostrará un mensaje de error.
4. Si no hay errores, se imprimirá el elemento en la posición 0 de la lista.

## Manejo de Excepciones

El programa maneja la siguiente excepción:

- **IndexError:** Si la lista está vacía o si se intenta acceder a un índice fuera del rango de la lista, se muestra un mensaje de error indicando que no hay elementos en la lista o que se está intentando acceder a un índice fuera del rango.

El bloque `finally` se utiliza para imprimir un mensaje de agradecimiento que se ejecutará siempre, independientemente de si se producen excepciones o no.

EJER 4:
# Función de Operación Matemática con Manejo de Excepciones


## Uso

La función `omatematica(a, b)` realiza una operación matemática entre los argumentos `a` y `b`. En este ejemplo, se realiza una suma. Si los argumentos no son del tipo de datos numéricos esperado, se generará una excepción TypeError.

## Manejo de Excepciones

La función maneja la siguiente excepción:

- **TypeError:** Si los argumentos no son del tipo de datos numéricos esperado, se muestra un mensaje de error indicando que los argumentos deben ser del tipo de datos numéricos.

El bloque `finally` se utiliza para imprimir un mensaje de agradecimiento que se ejecutará siempre, independientemente de si se producen excepciones o no.

## Ejemplo de Uso

```python
# Ejemplos
operacion_matematica(5, 3)  # funciona correctamente
operacion_matematica("Hola", 3)  # funciona incorrectamente






