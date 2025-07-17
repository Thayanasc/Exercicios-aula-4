#Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float (input('Digite um numero'))
n2 = float (input('Digite um numero'))
n3 = float (input('Digite um numero'))

maior = max (n1,n2,n3)
menor = min(n1, n2, n3)

#coloque para imprimir
if maior == int(maior):
    maior=int(maior)

if menor == int(menor):
    menor = int(menor)

#os resultados
print("O maior número é:", maior)
print("O menor número é:", menor)
