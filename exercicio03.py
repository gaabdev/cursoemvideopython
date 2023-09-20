#Faça um programa que leia um número inteiro e que mostre na tela o seu sucessor e antecessor


numero = int(input("Digite um número: "))
antecessor = numero - 1
sucessor = numero + 1

print("Analisando o valor {}, seu antecessor é {} e seu sucessor é {}".format(numero, antecessor, sucessor))