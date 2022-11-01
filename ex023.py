#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos algarismos separados.
n = str(input('digite um numero (1 a 9999): '))
if (int(n) <= 9999):
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format((n[0]),(n[1]),(n[2]),(n[3])))
else:
    print('Numero além do limite!')
