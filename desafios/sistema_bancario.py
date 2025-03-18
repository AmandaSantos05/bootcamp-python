menu = """
==== Menu ====
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = """
==== Extrato ====
"""


while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Digite o valor do depósito:\n"))
        saldo += deposito
        extrato += f"- {deposito}\n"
        print(saldo)

    elif opcao == "2":
        print("Saque")

    elif opcao == "3":
        print(extrato)

    elif opcao == "0":
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")