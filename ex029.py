#029: Escreva um programa que leia a velocidade de um carro. -Se ele ultrapassar 80Km/, mostre uma mensagem dizendo que ele foi multado. -A multa vai custar R$7,00 por cada Km acima do limite.
v = int(input('Você passou por um radar de 80Km/h! declare sua velocidade: '))
if v <= 80:
    print('Ainda bem que você viu a tempo! você não foi multado.')
elif v <= 400:
    print('Você foi multado no valor de R${}. Preste mais atenção!'.format((v-79)*7))
else:
    print('Tá querendo ir pra Lua, amigão ?')
