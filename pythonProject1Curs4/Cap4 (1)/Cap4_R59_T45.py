"""
459
Crearea unei functii simple
PF 25.09.2020 v4
"""  #

# pylint: disable=invalid-name
# pylint: disable=unidiomatic-typecheck

enunt = """Creati o functie care sa calculeze si sa returneze (a*(a+3)/b)*c,
pentru 3 numere a, b, c.
Daca nu sunt numere va returna: "Parametrii trebuie sa fie numere: ":
"""

def expresie(a, b, c):
    """Calculeaza [a(a+3)/b]*c"""
    if type(a) == type(b) == type(c) == type(2):
        x = (a * (a + 3) / b) * c
    else:
        x = "Parametrii trebuie sa fie numere"
    return x


expresie(1, 2, 3)

expresie("1", "2", "3")

# expresie(1, 2, 3, 4, 5, 6, 76)

input("\n\nApasa enter pentru a iesi")
