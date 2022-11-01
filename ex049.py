# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um numero: '))
l = 1
for l in range(1,11):
    print('{} vezes {} é {}'.format(n, l, n*l))