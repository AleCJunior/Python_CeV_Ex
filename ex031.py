# 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule e peça o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
km = float(input('Qual é a distancia da viagem, em Km?: '))
if km <= 200:
    km = (km*0.5)
else:
    km = (km * 0.45)
print('A viagem irá custar R${:.2f}'.format(km))
