# Exercício Python 071. Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
# serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cedulas = [200, 100, 50, 20, 10, 5, 2, 1]
resto = div = c1 = c2 = stg = 0
lista = []
# ----------------------------------------------------------------------------------------------------------------------
val = input('Qual será o valor sacado ?\nR$')
while val.isnumeric() is False or int(len(val.split())) != 1:
    val = input('Valor digitado é invalido! Tente novamente: R$')
# ----------------------------------------------------------------------------------------------------------------------
vc = int(val)
resto = vc
# ----------------------------------------------------------------------------------------------------------------------
while True:
    div = resto // cedulas[c1]
    resto = resto % cedulas[c1]
    lista.append(div)
    if lista[c1] != 0:
        print(f'Notas de R${cedulas[c1]}: {lista[c1]}')
    if resto == 0:
        break
    c1 = c1 + 1
