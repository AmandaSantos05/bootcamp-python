# Um conjunto com elementos que estão em um dos conjuntos, mas não em ambos.
# Use o método symmetric_difference() ou ^

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)

resultado2 = conjunto_b ^ conjunto_a
print(resultado2)