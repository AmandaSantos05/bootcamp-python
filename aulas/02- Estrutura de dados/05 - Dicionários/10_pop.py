# Remove um elemento do dicionário com base em sua chave

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {}) # {}  # Se a chave nã existir, retorna o valor informado como segundo parâmetro
print(resultado)
