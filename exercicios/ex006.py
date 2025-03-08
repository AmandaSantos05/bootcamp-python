# Ler um número inteiro. Se o número lido for negativo, escreva a mensagem “Número
# inválido”. Se o número for positivo, calcular o logaritmo natural deste numero.
import math

num = int(input("Informe um número inteiro: "))

if num < 0:
    print("Número inválido")
else:
    num_log = math.log(num)
    print(f"O logaritmo natural de {num} é: {num_log}")