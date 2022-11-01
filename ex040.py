#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
nome = str(input('Digite seu nome:\n'))
n1 = int(input('Digite a primeira nota:\n'))
n2 = int(input('Digite a segunda nota:\n'))
media = ((n1 + n2) / 2)
if media < 5:
    print('Parabens {}, sua media é {}, você foi REPROVADO!'.format(nome, media))
elif 5 >= media >= 6.9:
    print('Parabens {}, sua media é {}, você está de recuperação!'.format(nome, media))
else:
    print('Parabens {}, sua media é {}, você foi APROVADO!'.format(nome, media))
