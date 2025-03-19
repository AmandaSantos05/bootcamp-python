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
        extrato += f"""
        ==== Extrato ====
        Depósito - {valor}\n"""
    elif tipo == "2":
        extrato += f"""
        ==== Extrato ====
        Saque - {valor}\n"""

def depositar():
    global saldo
    deposito = float(input("Informe o valor do depósito:\n"))
    saldo += deposito
    registrar_transacao("1", deposito)
    return deposito

def sacar():
    global saldo, limite, numero_saques
    if numero_saques > 3: print("Limite de saque excedido!")
    saque = float(input("Informe o valor do saque:\n"))
    if saldo < saque: print("Saldo insuficiente!")
    if saque > limite: print("Limite por saque é R$500,00")

    saldo -= saque
    registrar_transacao("2", saque)
    numero_saques += 1
        
    


while True:
    opcao = input(menu)

    if opcao == "1":
        depositar()
        print("Depósito realizado com sucesso!")

    elif opcao == "2":
        sacar()
        print("Saque realizado com sucesso!")

    elif opcao == "3":
        if extrato == "":
            print("Não foram realizadas movimentações")
        
        print(extrato)

    elif opcao == "0":
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")