#  Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
#  peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
#   Homens: (72.7 * h) - 58
#   Mulheres: (62.1 * h) - 44.7

sexo = input("Qual teu sexo? \nMasculino [M]\nFeminino [F]\n")
altura = float(input("Informe sua altura: "))

peso_ideal_m = round((72.7 * altura) - 58)
peso_ideal_f = round((62.1 * altura) - 44.7)

if sexo.upper() == "M":
    print(f"Seu peso ideal é {peso_ideal_m}")
elif sexo.upper() == "F":
    print(f"Seu peso ideal é {peso_ideal_f}")
else:
    print("Sexo inválido!")