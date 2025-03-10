import sys
# EXEMPLO 1
# saldo = 2000.0
# opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato: \n"))

# if opcao == 1:
#     valor = float(input("Informe o valor do saque: \n"))
#     if valor <= saldo:
#         saldo -= valor
#         print("Saque Realizado!")
#         print(saldo)
#     else:
#         print("Saldo Insuficiente!")
# elif opcao == 2:
#     print(saldo)
# else:
#     sys.exit("Opção inválida")

#-----------------------------------------

#EXEMPLO 2
MAIOR_IDADE = 18
idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")

else:
    print("Ainda não pode tirar a CNH.")