"""
Escribe una funcion que recibe dos palabras y retorne verdadero o falso segun sea o no anagramas.
- Un anagrama consiste en formar una palabra reordenando todas las letras de otra palabra inicial.
- No hace falta comprobar que ambas palabras existan
- Dos palabras exactamente iguales no son anagramas
"""
def anagrama(palabra1: str, palabra2: str):
    if palabra1.lower() ==  palabra2.lower():
        return False
    
    return sorted(palabra1.lower()) == sorted(palabra2.lower())
    
print(anagrama('amor', 'Roma'))