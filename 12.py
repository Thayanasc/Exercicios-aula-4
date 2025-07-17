# Entrada de dados
valor_hora = float(input("Digite o valor da sua hora: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

# Cálculo do salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Definição das alíquotas
inss = salario_bruto * 0.10
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11  # Não desconta
total_descontos = 0
ir = 0
ir_percentual = 0

# Cálculo do IR conforme a faixa salarial
if salario_bruto <= 900:
    ir = 0
    ir_percentual = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
    ir_percentual = 5
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
    ir_percentual = 10
else:
    ir = salario_bruto * 0.20
    ir_percentual = 20

# Soma dos descontos (IR + INSS + Sindicato)
total_descontos = ir + inss + sindicato

# Cálculo do salário líquido
salario_liquido = salario_bruto - total_descontos

# Impressão formatada dos resultados
print("\n--- Folha de Pagamento ---")
print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir_percentual}%) : R$ {ir:.2f}")
print(f"(-) INSS (10%) : R$ {inss:.2f}")
print(f"(-) Sindicato (3%) : R$ {sindicato:.2f}")
print(f"FGTS (11%) : R$ {fgts:.2f}")
print(f"Total de descontos : R$ {total_descontos:.2f}")
print(f"Salário Líquido : R$ {salario_liquido:.2f}")