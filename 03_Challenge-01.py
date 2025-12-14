"""
Escribe un programa que muestre por consola los numeros de 1 a 100 (ambos incluidos y con un salto de linea entre cada impresion, sustituyendo los siguientes:
- Multiplos de 3 por la palabra 'fizz'
- Multiplos de 5 por la palabra 'buzz'
- Multiplos de 3 y 5 a la vez por la palabra 'fizzbuzz'
"""

def fizzbuzz():
    """Muestra los numeros del 1 al 100 con las sustituciones indicadas."""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{i} -> {'fizzbuzz'}')
        elif i % 3 == 0:
            print(f'{i} -> {'fizz'}')
        elif i % 5 == 0:
            print(f'{i} -> {'buzz'}')
        else:
            print(i)

fizzbuzz()