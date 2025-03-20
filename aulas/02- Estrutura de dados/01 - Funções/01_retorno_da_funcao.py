def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([10, 20,34]))

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(retorna_antecessor_e_sucessor(10))