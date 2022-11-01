# Exercício Python 060. Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = input('Digite um numero inteiro, para descobrir seu fatorial!\n: ')
while num.isnumeric() is False or len(num.split()) != 1:
    num = input('Dado invalido! digite novamente\n: ')

c = 0
f = int(num)
vf = []
vt = 1

while c != f:
    c = c + 1
    vf.append(c)

for t in range(1, f):
    vt = vt * c
    c = c - 1

vl = str(str(vf[::-1]).strip('[').strip(']'))

print('Fatorial de {}!\n{} = {}'.format(f, vl.replace(', ', ' x '), vt))
