# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente
# a este numero. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

dia = -1

while dia != 0:
    dia = int(input("Digite um número para escolher um dia:\n[1] Domingo\n[2] Segunda-feira\n[3] Terça-feira\n[4] Quarta-feira\n[5] Quinta-feira\n[6] Sexta-feira\n[7] Sábado\n[0] Sair\n-> "))

    if dia == 1:
        print("Domingo\n\n")
    elif dia == 2:
        print("Segunda-feira\n\n")
    elif dia == 3:
        print("Terça-feira\n\n")
    elif dia == 4:
        print("Quarta-feira\n\n")
    elif dia == 5:
        print("Quinta-feira\n\n")
    elif dia == 6:
        print("Sexta-feira\n\n")
    elif dia == 7:
        print("Sábado\n\n")
else:
    print("Boa semana!")