# Exercício Python 37: Escreva um programa em Python
# que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um numero:\n'))
print('''Escolha a opção de conversão desejada
[ 1 ] Converter para binário
[ 2 ] Converter para octal
[ 3 ] Converter para hexadecimal''')
op = int(input(' '))
if op == 1:
    print('{} Convertido para binário é {}'.format((num), (bin(num))))
elif op == 2:
    print('{} Convertido para octal é {}'.format((num), (oct(num))))
elif op == 3:
    print('{} COnvertido para hexadecimal é {}'.format((num), (hex(num))))
else:
    print('Opção invalida')

