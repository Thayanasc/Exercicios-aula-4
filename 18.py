from datetime import datetime

# Solicita a data ao usuário
data_input = input("Digite uma data no formato dd/mm/aaaa: ")

# Tenta converter a data
try:
    data = datetime.strptime(data_input, "%d/%m/%Y")
    print(f"A data {data_input} é válida.")
except ValueError:
    print(f"A data {data_input} é inválida.")
