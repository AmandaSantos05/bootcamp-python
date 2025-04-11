# Outra forma de adicionar valores no dicionario

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError - Se a chave informada não existir, uma exceção é lançada

print(contatos.get("chave"))  # Se a chave informada não existir, retorna None
print(contatos.get("chave", {}))  # Mas pode ser informado um segundo argumento, se ele não encontrar a chave, retorna o valor informado como segundo argumento.
print(contatos.get("guilherme@gmail.com", {})) # {'nome': 'Guilherme', 'telefone': '3333-2221'}