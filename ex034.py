# 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. -Para salários
# superiores a R$1.250,00, calcule um aumento de 10%. -Para os inferiores ou iguais, o aumento é de 15%
n1 = float(input('Quanto você ganha ?: '))
if n1 > 1250:
    n1 = n1*1.10
else:
    n1 = n1*1.15
print('Você recebeu um re-ajuste! Seu salario agora é R${:.2f}'.format(n1))
