# Exercício Python 36: Escreva um programa para aprovar o empréstimo
# bancário para a compra de uma casa. Pergunte o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
# do salário ou então o empréstimo será negado.
nome = str(input('\033[1;97;40m Qual é o seu nome ? \033[m \n: '))
sal = float(input('\033[1;97;40m Qual é o seu salario ?: \033[m \n: '))
valor = float(input('\033[1;97;40m Qual é o Valor da casa ? \033[m \n: '))
anos = int(input('\033[1;97;40m Em quantos anos você vai pagar ? \033[m \n: '))
if (sal*0.3) >= (valor / (anos*12)):
    print('\033[1;30;42m Parabens {}, seu emprestimo foi aprovado! \033[m'.format(nome))
else:
    print('\033[1;30;41m Sinto muito, {}, seu emprestimo foi negado. \033[m'.format(nome))
