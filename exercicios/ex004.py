# Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
#  prestação for maior que 20% do salário imprima: Emprestimo não concedido, caso
#  contrário imprima: Emprestimo concedido.

salario = 2000
prestacao_emprestimo = 400

porcentagem_salario = salario * 0.20

if prestacao_emprestimo >= porcentagem_salario:
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")