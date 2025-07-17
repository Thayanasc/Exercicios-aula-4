#Faça um Programa que leia três números e mostre o maior deles.
n1 = float (input('Digite um numero'))
n2 = float (input('Digite um numero'))
n3 = float (input('Digite um numero'))

maior = max (n1,n2,n3)

if maior == int(maior):
    print ("o maior numero é: ", int(maior))
    
else:
    print ('o maior numero é:", maior')

           