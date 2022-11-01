# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a
# razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

inicio = int(input('Digite o numero inicial: '))
razao = int(input('Digite a razão: '))
for c in range(inicio, (10 * razao) + inicio, razao):
    print(c, end=' -> ')
print(end='Acabou')
