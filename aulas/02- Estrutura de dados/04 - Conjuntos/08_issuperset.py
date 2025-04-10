# Determina se um conjunto é um superconjunto do outro
# Usa o método issuperset() ou >=

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)

resultado = conjunto_b >= conjunto_a  # True
print(resultado)