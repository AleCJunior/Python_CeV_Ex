#033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n = str(input('Digite tres numeros separados por espaço: '))
l = n.split()
print('O menor é {}, o maior é {}'.format((min(l)), (max(l))))
