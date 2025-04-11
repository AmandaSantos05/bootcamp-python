# Fromkeys cria chaves.
# É útil em duas situações:
# 1- Criar chave sem vincular valor;
# 2- Criar um cojunto de chaves e colocar um valor padrão nelas.

resultado = dict.fromkeys(["nome", "telefone"])
print(resultado)  # {'nome': None, 'telefone': None}

resultado = dict.fromkeys(["nome", "telefone"], "vazio")
print(resultado)  # {'nome': 'vazio', 'telefone': 'vazio'}