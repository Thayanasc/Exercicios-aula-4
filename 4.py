#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = (input('digite uma letra'))

if len(letra) == 1 and letra.isalpha():
    if letra in ['a', 'e', 'i', 'o', 'u']:
        print("A letra é uma vogal.")
    else:
        print("A letra é uma consoante.")

     