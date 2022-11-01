#028. Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o número escolhido pelo computador. -O programa deverá escrever na tela se o usúario venceu ou perdeu.
import random
n1 = int(input('Digite o intervalo de dois numeros, separadamente, e o computador ira sortear um numero entre eles, tente advinhar!\nInicial: '))
n2 = int(input('Final: '))
nr = round(random.uniform(n1, n2))
nc = int(input('Agora tente advinhar o numero: '))
if nc == nr:
    print('Parabens, você acertou!')
else:
    print('Infelizmente você errou. O numero era {}'.format(nr))
