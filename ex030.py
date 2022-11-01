#030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = str(input('Manda um numero po pai aquikkkk (só pode numero inteito): '))
pair = ('0', '2', '4', '6', '8') #Uma lista de numeros em texto!
if n != '0':
    if n.endswith(pair):
        print('O numero que você digitou é par')
    else:
        print('O Numero que você digitou não é par')
else:
    print('O numero é neutro')
