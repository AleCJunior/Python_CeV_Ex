#032: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
n = int(input('Em que ano estamos?\n: '))
n = n / 4
if str(n).endswith('.0'):
    print('É um ano bisexto')
else:
    print('e a chuva ein? kkkk')
