# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

valor = float(input('Qual é o valor do produto?\n: R$'))
pgt = input('Qual é a forma de pagamento ?\n[ 1 ] DINHEIRO / CHEQUE\n[ 2 ] A VISTA NO CARTÃO\n[ 3 ] EM ATÉ 2 VEZES NO CARTÃO\n[ 4 ]EM 3 VEZES OU MAIS NO CARTÃO\n: ')
if pgt.isnumeric() and 0 < int(pgt) < 5:
    pgt = int(pgt)
    if pgt == 1:
        print('O valor a ser pago será de R${:.2f}'.format(valor*0.9))
    elif pgt == 2:
        print('O valor a ser pago será de R${:.2f}'.format(valor * 0.95))
    elif pgt == 3:
        print('O valor a ser pago será de R${:.2f}'.format(valor))
    elif pgt == 4:
        print('O valor a ser pago será de R${:.2f}'.format(valor * 1.2))
else:
    print('A opção escolhida é invalida.')
