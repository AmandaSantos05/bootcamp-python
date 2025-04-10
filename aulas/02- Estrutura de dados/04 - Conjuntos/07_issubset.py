# Verificar se um elemento ou conjunto é subconjunto do outro
# Pode usar o operador in ou issubset()

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(2 in conjunto_a)

resultado = conjunto_a.issubset(conjunto_b)
print(resultado)
resultado = conjunto_b.issubset(conjunto_a)
print(resultado)