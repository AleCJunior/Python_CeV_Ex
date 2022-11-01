# Exercício Python 68. Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

v = 0

print("""Bem vindo ao jogo do par ou impar! Para jogar, basta digitar "Par" ou "Impar" e em sequencia, seu numero.
O computador irá escolher um valor entre 1 e 100, e então o resultado sairá!""")

while True:
    pg = input('[ 0 ] PAR / [ 1 ] IMPAR: ')
    while pg.isnumeric() is False or int(pg) < 0 or int(pg) > 1:
        pg = input('Dados invalidos! digite novamente: ')

    pn = input('Agora escolha um numero!: ')
    while pn.isnumeric() is False or int(len(pn.split())) != 1:
        pg = input('Valor invalido! Tente novamente: ')
    pn = int(pn)

    mn = randint(1, 100)
    print(f'A maquina escolheu {mn}')

    for c in range(1, 4):
        sleep(0.3)
        print('.', end='')
    sleep(0.3)

    print(f' {pn} + {mn} = {pn + mn}.', end=' ')
    if ((pn + mn) % 2) == int(pg):
        if int(pg) == 0:
            print('Você escolheu PAR e ganhou!')
        else:
            print('Você escolheu IMPAR e ganhou!')
        v = v + 1
    else:
        if int(pg) == 0:
            print('Você escolheu PAR e perdeu.')
        else:
            print('Você escolheu IMPAR e perdeu.')
        if v == 0:
            print('Mais sorte na proxima!')
            break
        else:
            print(f'Você teve {v} vitorias consecutivas! parabens')
            break
