# Exercício Python 72. Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. O seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

ext1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
ext2 = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
ext3 = ('vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa', 'cem')

# DEZENA----------------------------------------------------------------------------------------------------------------

keep = 'S'

while keep.upper() == 'S':
    dezena = centena = ne = []
    num = input('Digite seu numero, para velo por extenso. [LIMITE: 99]\n: ')
    while num.isnumeric() is False or len(num.split()) != 1 or int(num) > 99:
        num = input('Valor digitado é invalido!: ')
    n = int(num)

    if 0 < n < 10:
        ne.append(ext1[int(num[0])])
        print(f'N. Extenso: {ne}')
    elif 9 < n < 20:
        ne.append(ext2[int(num[1])])
        print(f'N. Extenso: {ne}')
    elif 19 < n < 100:
        if int(num[1]) == 0:
            ne.append(ext3[int(num[0]) - 2])
            print(f'N. Extenso: {ne}')
        else:
            ne.append(ext1[int(num[1])])
            ne.append('e')
            ne.append(ext3[int(num[0]) - 2])
            print(f'N. Extenso: {ne[2]} {ne[1]} {ne[0]}')
    keep = input('Deseja continuar ?[S/N]: ')
    while keep.upper() not in 'SN':
        keep = input('Resposta invalida! tente novamente: ')
