# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um numero: '))
l = 1
for l in range(1,11):
    print('{} vezes {} é {}'.format(n, l, n*l))
