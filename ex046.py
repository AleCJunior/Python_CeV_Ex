# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o
# estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('Você acabou de acender os fogos de artificio! eles vão estourar em...')
tempo = int(10)
for c in range(0, 10):
    print(tempo)
    sleep(1)
    tempo = tempo - 1
print('Não solte fogos de artificio! pense nos animais')
