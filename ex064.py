# Exercício Python 64. Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


num = c = soma = c2 = 0
tot = []

print('Digite um numero. Digite "999" para parar.')
while num != 999:
    n = input('-> ')
    while n.isnumeric() is False or int(len(n.split())) != 1:
        n = input('Dados invalido! digite novamente: ')
    num = int(n)
    tot.append(n)
    c = c + 1

while c2 <= c - 1:
    soma = soma + int(tot[c2])
    c2 = c2 + 1

c = c - 1
soma = soma - 999

print('A soma de todos os {} valores digitados é igual a {}'.format(c, soma))
