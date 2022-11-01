brl = float(input('Quanto dinheiro você tem?\n'))
if brl >= 3.27:
    print('Você pode comprar U${:.3f}'.format(brl/3.27))
else:
    print('Você não pode comprar nenhum dólar')
