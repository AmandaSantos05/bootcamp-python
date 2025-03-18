menu = """
==== Menu ====
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0.0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = """
==== Extrato ====
"""

def registrar_extrato(tipo, valor):
    global extrato
    if tipo == "1":
        extrato += f"Depósito - {valor}\n"
    elif tipo == "2":
        extrato += f"Saque - {valor}\n"

def depositar():
    global saldo
    deposito = float(input("Informe o valor do depósito:\n"))
    saldo += deposito
    registrar_extrato("1", deposito)
    return deposito

# def sacar():
#     global saldo
    


while True:
    opcao = input(menu)

    if opcao == "1":
        depositar()
        print("Depósito realizado com sucesso!")

    elif opcao == "2":
        numero_saques += 1
        if numero_saques > 3:
            print("Saque")

    elif opcao == "3":
        print(extrato)

    elif opcao == "0":
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")