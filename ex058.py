# Exercício Python 58. Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” num número entre 0 e 10.
# Entretanto, agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint

# ----------------------- VALIDAÇÃO DE LIMITES ----------------------------

lim = input('Digite os dois valores de limite, inicial e final\n: ')
while ((lim.replace(' ', '')).isnumeric() is False) or (len(lim.split()) != 2) or ('0' in lim is True):
    lim = input('Valor invalido! digite novamente.\n: ')
lista = lim.split()
if lista[0] > lista[1]:
    lista = lista[::-1]
ls = lista

# ------------------------ CONTROLE DE VARIAVEIS --------------------------

mg = randint(int(ls[0]), int(ls[1]))
tentativa = 1

# ------------------------------ GAME --------------------------------------

pg = input('agora tente advinhar o valor escolhido pela maquina!\n: ')

while (pg.replace(' ', '')).isnumeric() is False or len(pg.split()) != 1:  # Validadador de entrada.
    pg = input('Valor digitado invalido! tente novamente.\n: ')

while int(pg) != int(mg):  # Condição de acerto + contagem

    while (pg.replace(' ', '')).isnumeric() is False or len(pg.split()) != 1:  # Validadador de entrada no acerto
        pg = input('Valor digitado invalido! tente novamente.\n: ')

    if int(pg) < mg:
        pg = input('Um pouco mais... tente denovo.\n: ')
    else:
        pg = input('Um pouco menos... tente denovo.\n: ')

    tentativa = tentativa + 1

print('Você acertou na {}ª tentativa! parabens'.format(tentativa))
