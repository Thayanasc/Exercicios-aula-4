# Leitura dos três lados
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

# Verifica se os lados podem formar um triângulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("\nOs lados formam um triângulo.")

    # Verifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("Tipo: Triângulo Equilátero (3 lados iguais)")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Tipo: Triângulo Isósceles (2 lados iguais)")
    else:
        print("Tipo: Triângulo Escaleno (3 lados diferentes)")
else:
    print("\nOs valores informados NÃO formam um triângulo.")
