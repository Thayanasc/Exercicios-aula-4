# Leitura das duas notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Determinação do conceito
if 9.0 <= media <= 10.0:
    conceito = "A"
    status = "APROVADO"
elif 7.5 <= media < 9.0:
    conceito = "B"
    status = "APROVADO"
elif 6.0 <= media < 7.5:
    conceito = "C"
    status = "APROVADO"
elif 4.0 <= media < 6.0:
    conceito = "D"
    status = "REPROVADO"
elif 0 <= media < 4.0:
    conceito = "E"
    status = "REPROVADO"
else:
    conceito = "-"
    status = "Média inválida!"

# Exibe os resultados
print("\n--- Resultado Final ---")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Situação: {status}")
