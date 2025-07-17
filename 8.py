#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
preço1= (input('digite o preco do primeiro produto'))
preço2= (input('digite o preco do segundo produto'))
preço3 =(input('digite o preco do terceiro produto'))

menor_preco = min(preço1, preço2 , preço3)

if menor_preco == preço1:
    print("Você deve comprar o primeiro produto.")
elif menor_preco == preço2:
    print("Você deve comprar o segundo produto.")
else:
    print("Você deve comprar o terceiro produto.")