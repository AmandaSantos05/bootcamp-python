def salvar_carro(marca, modelo, ano, placa):
    print(f"""Carro inserido com sucesso! 
    Marca: {marca}
    Modelo: {modelo}
    Ano: {ano}
    Placa: {placa}\n""")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca":"Fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1234"})



def cadastrar_funcionario(nome, ano_nasc, cpf):
    print(f"""Funcionário cadastrado com sucesso!
    Nome: {nome}
    Ano de Nascimento: {ano_nasc}
    CPF: {cpf}""")

cadastrar_funcionario(nome="Amanda Santos", ano_nasc=1996, cpf= "99999999999")