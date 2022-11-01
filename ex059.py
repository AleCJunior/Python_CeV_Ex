# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# O seu programa deverá realizar a operação solicitada em cada caso.


v = input('Digite os dois valores a serem operados, da seguinte forma: "1 2"\n: ')
while False == (v.replace(' ', '')).isnumeric() or len(v.split()) != 2:
    v = input('Valor digitado invalido, tente denovo\n: ')
vs = v.split(' ')

option = 0

print('Escolha a operação desejada:')

while option != '5':
    print('-' * 20)
    option = input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Escolher outros numeros\n[5] Sair do programa\n: ')
    print('-' * 20)
    if option == '1':
        print(' A soma entre {} e {} é de {}'.format(vs[0], vs[1], int(vs[0]) + int(vs[1])))
    elif option == '2':
        print(' A multiplicação entre {} e {} é de {}'.format(vs[0], vs[1], int(vs[0]) * int(vs[1])))
    elif option == '3':
        if int(vs[0]) > int(vs[1]):
            print('entre {} e {}, o maior é {}'.format(vs[0], vs[1], vs[0]))
        elif int(vs[0]) < int(vs[1]):
            print('entre {} e {}, o maior é {}'.format(vs[0], vs[1], vs[1]))
        else:
            print('os valores {} e {} são iguais'.format(vs[0], vs[1]))
    elif option == '4':
        v = input('Digite os dois valores a serem operados, da seguinte forma: "1 2"\n: ')
        while False == (v.replace(' ', '')).isnumeric() or len(v.split()) != 2:
            v = input('Valor digitado invalido, tente denovo\n: ')
        vs = v.split(' ')
