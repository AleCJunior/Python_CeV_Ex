#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

print("""Bem vindo ao jogo do Jokenpo! Você vai jogar contra a maquina. Escolha uma das opções abaixo
[ 1 ] Jó ( PEDRA )
[ 2 ] Ken ( PAPEL )
[ 3 ] Po ( TESOURA )""")
jokenpo = ['0', 'PEDRA', 'PAPEL', 'TESOURA']
voce = input(': ')
maquina = int(randint(1, 3))
if voce.isnumeric() and 0 < int(voce) < 4:
    voce = int(voce)
    print('Você escolheu: "{}"\nA maquina escolheu "{}"'.format(jokenpo[(voce)], jokenpo[(maquina)]))
    win = ('\033[7;30;42m VOCÊ GANHOU! \033[m')
    if voce == maquina:
        print('\033[7;49;37m EMPATE! \033[m')
    elif voce == 1 and maquina == 3:
        print(win)
    elif voce == 2 and maquina == 1:
        print(win)
    elif voce == 3 and maquina == 2:
        print(win)
    else:
        print('\033[7;30;41m A MAQUINA GANHOU \033[m')
else:
    print('O valor escolhido é invalido')
