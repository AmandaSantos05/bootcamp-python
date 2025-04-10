# Cria um novo conjunto contendo apenas elementos que estão no primeiro conjunto, mas não no segundo.
# Utiliza o método difference() ou -

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado2 = conjunto_b - conjunto_a
print(resultado2)