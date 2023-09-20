#Crie um algoritmo que leia um número e mostre ser dobro, triplo e raiz quadrada

numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raizquadrada = numero **0.5

print("O dobro de {} vale {}".format(numero, dobro))
print("O triplo de {} vale é {}".format(numero, triplo))
print("A raiz quadrada de {} é igual a {:.2f}".format(numero, raizquadrada))


import math

n = int(input("Digite um número: "))
raiz = math.sqrt(n)
print(raiz)