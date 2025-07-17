#Faça um Programa que peça dois números e imprima o maior deles.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# Verifica se os números são iguais
if n1 == n2:
    print("Os dois números são iguais.")
else:
    # Determina o maior número
    maior = n1 if n1 > n2 else n2

    #o número for inteiro (ex: 7.0), converte para int
    if maior == int(maior):
        print("O maior número é:", int(maior))
    else:
        print("O maior número é:", maior)