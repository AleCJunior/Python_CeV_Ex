nome = str(input('Funcionário: \n'))
sar = float(input('Seu sálario:\n'))
print('Parece que o seu salário está abaixo do piso permitido, você teve um acréscimo de 15%!\nValor do salário alterado para R${:.2f}'.format(sar*1.15))
