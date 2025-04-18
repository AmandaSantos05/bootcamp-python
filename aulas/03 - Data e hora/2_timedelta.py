from datetime import timedelta, datetime, date

tipo_carro = "P" # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará proto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará proto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará proto às {data_estimada}")

print(date.today() - timedelta(days=1))  #  Manipular data. Saída -> 2025-04-15 (data atual 16/04/2025)

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)  # Manipular hora (hora atual - 1 hora)... Constrói o timedelta
print(resultado.time())