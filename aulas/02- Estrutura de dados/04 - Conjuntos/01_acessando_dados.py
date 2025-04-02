# Conjuntos em Python não suportam indexação e nem fatiamento.
# Pra acessar os valores é necessário converter o conjunto em lista.
# É possível adicionar e remover elementos de um set

numeros = {1, 2, 3, 2}
numeros = list(numeros)

print(numeros[0])