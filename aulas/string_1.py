# MAIÚSCULA, MINÚSCULA E TÍTULO
nome = "AmAnDa"

print(nome.upper())
print(nome.lower())
print(nome.title())
print()

# ELIMINANDO ESPAÇOS EM BRANCO
texto = "  Olá mundo!    "
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")
print()

# JUNÇÕES E CENTRALIZAÇÃO
menu = "Python"

print(menu.center(14, "%"))
print("-".join(menu))