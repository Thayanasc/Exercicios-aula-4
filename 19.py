# Lê o número
numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000 or numero < 0:
    print("Número inválido! Digite um número entre 0 e 999.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    # Centenas
    if centenas > 0:
        if centenas == 1:
            partes.append("1 centena")
        else:
            partes.append(f"{centenas} centenas")

    # Dezenas
    if dezenas > 0:
        if dezenas == 1:
            partes.append("1 dezena")
        else:
            partes.append(f"{dezenas} dezenas")

    # Unidades
    if unidades > 0:
        if unidades == 1:
            partes.append("1 unidade")
        else:
            partes.append(f"{unidades} unidades")

    # Se o número for zero
    if numero == 0:
        print("0 unidades")
    else:
        # Monta a frase corretamente com vírgula e 'e'
        if len(partes) == 1:
            print(f"{numero} = {partes[0]}")
        elif len(partes) == 2:
            print(f"{numero} = {partes[0]} e {partes[1]}")
        else:
            print(f"{numero} = {partes[0]}, {partes[1]} e {partes[2]}")
