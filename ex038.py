# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais
n1 = (input('Digite um numero inteiro:\n'))
n2 = (input('Digite outro numero inteiro:\n'))
if n1.isnumeric():
    if n2.isnumeric():
        if n1 > n2:
            print('o valor {} é maior que o valor {}'.format((n1), (n2)))
        elif n1 < n2:
            print('O valor {} é menor que o valor {}'.format((n1), (n2)))
        else:
            print('Os dois valores são iguais')
else:
    print('Os valores digitados não são numeros inteiros.')
