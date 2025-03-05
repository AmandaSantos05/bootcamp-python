# 1. Faça um programa que receba dois números e mostre qual deles é o maior.

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
maior_numero = 0

if num1 > num2:
    print("O maior número é ", num1)
elif num2 > num1:
    print("O maior número é ", num2)
else:
    print("Números iguais!")