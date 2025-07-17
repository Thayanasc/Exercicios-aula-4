# Solicita o salário atual do colaborador
salario = float(input("Digite o salário atual do colaborador: R$ "))

# Define as faixas e os percentuais de aumento
if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

# Calcula o valor do aumento e o novo salário
aumento = salario * (percentual / 100)
novo_salario = salario + aumento

# Mostra as informações detalhadas
print("\n--- Detalhamento do Reajuste ---")
print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")
