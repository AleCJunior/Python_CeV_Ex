# Crie um programa que faça o computador jogar Jokenpô com você. V2!

from random import randint

print("""Bem vindo ao jogo do Jokenpo! Você vai jogar contra a maquina. Escolha uma das opções abaixo
[ 1 ] Jó ( PEDRA )
[ 2 ] Ken ( PAPEL )
[ 3 ] Po ( TESOURA )""")
jokenpo = ['0', 'PEDRA', 'PAPEL', 'TESOURA']
voce = str(input('Deseja jogar o modo infinito ? digite SIM ou NAO\n: '))


def jkp():
    voce = input('OPÇÂO: ')
    maquina = int(randint(1, 3))
    if voce != 'PARAR':
        voce = int(voce)
        print('Você escolheu: "{}"\nA maquina escolheu "{}"'.format(jokenpo[voce], jokenpo[maquina]))
        if voce == maquina:
            print('\033[7;49;37m EMPATE! \033[m')
            return 1
        elif (voce == 1 and maquina == 3) or (voce == 2 and maquina == 1) or (voce == 3 and maquina == 2):
            print('\033[7;30;42m VOCÊ GANHOU! \033[m')
            return 2
        else:
            print('\033[7;30;41m A MAQUINA GANHOU \033[m')
            return 3
    else:
        exit()


if voce == 'SIM':
    win = int(0)
    lost = int(0)
    draw = int(0)
    print('Se desejar parar, digite "PARAR" no lugar da escolha.')
    while voce == 'SIM':
        state = (jkp())
        if state == 1:
            draw = draw + 1
        elif state == 2:
            win = win + 1
        elif state == 3:
            lost = lost + 1
        print('PLACAR: VITORIAS = {} / DERROTAS = {} / EMPATES = {}'.format(win, lost, draw))
else:
    jkp()
