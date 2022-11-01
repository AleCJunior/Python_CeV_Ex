# Exercício Python 63. Escreva um programa que leia um número N inteiro qualquer e mostre
# na tela os N primeiros elementos de uma Sequência de Fibonacci.

# Perdi no Ex63, tive que procurar a solução online.

entry = input('Quantas progressões da sequencia de fibonnaci você quer ? tem que ser no minimo 4.\n: ')
while entry.isnumeric() is False or len(entry.split()) != 1 or int(entry) <= 3:
    entry = input('Dados invalidos! insira novamente: ')

n = int(entry)
t1 = 0
t2 = 1
c = 3
print('{} -> {}'.format(t1, t2), end='')
while c <= n:
    t3 = t1 + t2
    print(' - > {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c = c + 1
