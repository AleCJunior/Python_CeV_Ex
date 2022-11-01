# Exercício Python 67. Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
c = cont = 0


def validate():
    global num
    while (num.strip('-')).isnumeric() is False or int(len(num.split())) != 1:
        if num.isnumeric() is False:
            num = input('Valor digitado é invalido, tente novamente: ')
        elif int(len(num.split())) != 1:
            num = input('É permitido digitar apenas um valor! digite novamente: ')


num = input("""Digite um valor para representar o limite da tabuada. Maximo de 30.
Para encerrar, digite um valor negativo.
: """)
validate()
if cont == 0:
    while 2 < int(num) > 30:
        if int(num) > 30:
            num = input('Valor de limite acima do permitido! tente novamente: ')
        elif 2 < int(num):
            num = input('Valor de limite abaixo do permitido! tente novamente: ')
    lim = int(num)
    cont = 1
while True:
    num = input(f'Digite um valor, para ver a sua tabuada, até {lim}: ')
    validate()
    if int(num) < 0:
        print('Fim do programa!')
        break
    else:
        c = 0
        while c <= lim:
            print(f'{num} X {c} = {int(num) * c}')
            c = c + 1
