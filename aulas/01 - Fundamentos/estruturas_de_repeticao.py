# # FOR

# texto = input("Informe um texto: ")
# VOGAIS = "AEIOU"

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end="")
# else:
#     print() #adiciona uma quebra de linha
#     print("Executa no final do laço")


# # Utilizando RANGE com FOR

# for numero in range(11):
#     print(numero, end=" ")


# for numero in range(0, 51, 5):
#     print(numero, end=" ")

# WHILE

# opcao = -1

# while opcao != 0:
#     opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

#     if opcao == 1:
#         print("Sacando...")
#     elif opcao == 2:
#         print("Exibindo o extrato...")
# else:
#     print("Obrigado por usar nosso Sistema Bancário, até logo!")


# While utilizando BREAK

# while True:
#     numero = int(input("Informe um número: "))

#     if numero == 10:
#         break

#     print(numero)


# While utilizando CONTINUE

for numero in range(11):

    if numero == 5:
        continue

    print(numero, end=" ")