"""
Imprima la sucesion de Fibonaci, imprima los primeros 50 numeros empezando desde 0
- La serie se compone por una sucesion de numeros en la que el siguiente siempres es la suma de los dos anteriores
"""

def fibonaci_serie(number: int):
    prev = 0
    next = 1
    for _ in range(number + 1):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


fibonaci_serie(50)