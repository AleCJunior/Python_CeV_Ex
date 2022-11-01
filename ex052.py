#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cont = int(0)
valor = int(input('Digite um valor: '))
for c in range(3, valor):
    if valor % c == 0:
        cont =+ 1
        print('{} é um divisor de {}'.format(c, valor))
if cont == 0:
    print('É um numero primo')
else:
    print('Não é um numero primo')
