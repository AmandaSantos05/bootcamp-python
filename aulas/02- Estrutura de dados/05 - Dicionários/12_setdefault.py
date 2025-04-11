# Adiciona uma chave e um valor a um dicionário, caso a chave não exista.
# Se a chave já existir, o método retorna o valor associado a ela.

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# contato.setdefault("nome", "Giovanna")
# print(contato) # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)
print(contato) # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}