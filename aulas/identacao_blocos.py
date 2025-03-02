#Indentar código é uma forma de manter o código fonte mais legível e manutenível.
#Em Python, através da indentação, o interpretador consegue determinar onde o bloco
#de comando inicia e onde ele termina.

def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("valor sacado!")


sacar(100)