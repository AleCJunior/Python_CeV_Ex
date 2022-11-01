#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

ag = int(date.today().year)
nas = (input('Em que ano você nasceu ?\n: '))
if nas.isnumeric():
    idade = ag - int(nas)
    if idade < 0:
        print('Ixpertinho! você ainda não nasceu')
    else:
        if idade == 0:
            print('O atleta não tem nem um ano ainda... tá cedo')
        else:
            print('O atleta tem {} anos'.format(idade))
        if idade <= 9:
            print('Classificação: MIRIM')
        elif idade <= 14:
            print('Classificação: INFANTIL')
        elif idade <= 19:
            print('Classificação: JÚNIOR')
        elif idade <= 25:
            print('Classificação: SÊNIOR')
        elif idade <= 120:
            print('Classificação: MASTER')
        else:
            print('Acho que você tá fazendo hora extra aqui.')
else:
    print('o valor digitado não é valido.')