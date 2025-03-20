#   FUNÇÕES DO SISTEMA
# 1. Depósito
# 2. Saque (limite de 3 saques, limite de 500,00 por saque, exibir mensagem se saldo negativo)
# 3. Extrato (exibir mensagem se o extrato estiver em branco)

menu = """
==== Menu ====
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0.0
limite = 500.0
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""


def registrar_transacao(tipo, valor):
    global extrato
    if tipo == "1":
        extrato += f"Depósito - R$ {valor}\n"
    elif tipo == "2":
        extrato += f"Saque - R$ {valor}\n"

def exibir_extrato():
    if extrato == "":
        print("Não foram realizadas movimentações")
        return
    else:
        print(extrato)

def depositar():
    global saldo
    deposito = float(input("Informe o valor do depósito:\n"))
    if deposito > 0:
        saldo += deposito
        registrar_transacao("1", deposito)
        print("Depósito realizado com sucesso!")
    else:
        print("Depósito inválido!")
    return deposito

def sacar():
    global saldo, limite, numero_saques
    if saldo <= 0:
        print("Não será possível realizar o saque por falta de saldo")
        return
    if numero_saques < 3: 
        saque = float(input("Informe o valor do saque:\n"))
    else:
        print("Limite de saque excedido!")
        return
    if saque > saldo: 
        print("Saldo insuficiente!")
        return
    if saque > limite: 
        print("Limite por saque é R$500,00")
        return

    saldo -= saque
    registrar_transacao("2", saque)
    numero_saques += 1
    print("Saque realizado com sucesso!")
        
    


while True:
    opcao = input(menu)

    if opcao == "1":
        depositar()

    elif opcao == "2":
        sacar()

    elif opcao == "3":
        exibir_extrato()

    elif opcao == "0":
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")