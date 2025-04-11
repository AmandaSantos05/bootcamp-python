# Remove elementos do dicionário
# Não recebe parâmetros

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

print(contatos.popitem()) # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})

print(contatos.popitem()) # KeyError  # Retorna exceção quando não encontra chave