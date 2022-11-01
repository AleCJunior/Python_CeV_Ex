# Exercício Python 70. Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
# se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

prod = []
compras = []
vt = ep = cp = c = c1 = 0
ncp = ' '

while True:
    desc = input('Nome: ')
    prod.append(desc)

    val = input('Preço: R$')
    while ((val.replace(',', '')).replace('.', '')).isnumeric() is False or int(len(val.split())) != 1:
        val = input('Valor digitado é invalido! Tente novamente: ')

    prod.append(f'R${val}')
    prod.append(float(val.replace(',', '.')))

    keep = input('Deseja Continuar? [S/N]: ')
    while keep.upper() not in 'SN' or int(len(keep.split())) != 1:
        keep = input('Resposta invalida! tente novamente: ')

    if keep == 'N':
        compras.append(prod)
        while c < int(len(compras)):
            vt = vt + float(compras[c][2])
            if c == 0 or float(compras[c][2]) < cp:
                cp = float(compras[c][2])
                ncp = (compras[c][0])
            if float(compras[c][2]) > 1000:
                c1 = c1 + 1
            c = c + 1
        print(f'O total gasto foi R${vt:.2}')
        print(f'Produtos que custam mais de R$1000: {c1}')
        print(f'{ncp} é o produto mais barato')
        break

    compras.append(prod)
    prod = []
