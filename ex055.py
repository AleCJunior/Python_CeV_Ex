# Exercício Python 55 - Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

cont = int(input('Quantas pesoas você deseja registrar o peso ?\n: '))
rp = []
pma = 0
pme = 0
for c in range(0, cont):
    peso = float(input('Insira o peso da {}ª pessoa: '.format(c + 1)))
    if c == 0:
        pme = peso
        pma = peso
        rp.append(peso)
    else:
        if peso > pma:
            pma = peso
            rp.append(peso)
        elif peso < pme:
            rp.append(peso)
            pme = peso
        else:
            rp.append(peso)
print('O maior peso registrado foi de {} Kg\nO menor peso registrado foi de {} Kg'.format(pma, pme))
print('Todos os pesos:\n', rp)
