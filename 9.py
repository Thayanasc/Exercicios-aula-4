#Faça um Programa que leia três números e mostre-os em ordem decrescente

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Coloca os números em uma lista
numeros = [n1, n2, n3]

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Remove o .0 se for número inteiro
numeros = [int(n) if n == int(n) else n for n in numeros]

# Exibe os números em ordem decrescente
print("Números em ordem decrescente:", numeros)