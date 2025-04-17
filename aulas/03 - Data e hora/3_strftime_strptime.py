from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2025-04-17 09:30"
mascara_ptbr = "%d/%m/%Y %A"
mascara_en = "%Y-%m-%d %H:%M"

data_formatada = data_hora_atual.strftime(mascara_ptbr)
print(f"Data formatada: {data_formatada}")

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(f"Data convertida: {data_convertida}")
print(type(data_convertida))