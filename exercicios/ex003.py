# 3. Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar

num = int(input("Informe um número inteiro: "))

if num % 2 == 0:
    print(num, "é par!")
else:
    print(num, "é ímpar!")