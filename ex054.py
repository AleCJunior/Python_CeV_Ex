# Exercício Python 54 Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
pessoas = []
maior = []
menor = []
mma = int(0)
mme = int(0)
cont = int(input('Quantas pessoas você ira registrar na media ?\n: '))
r = '0000'
for c in range(0, cont):
    if len(r) == 4 and r.isnumeric():
        r = input('Registre o ano de nascimento da {}ª pessoa: '.format(c + 1))
        pessoas.append(r)
        if (atual - int(r)) > 18:
            maior.append(atual - int(r))
            mma = mma + (atual - int(r))
        elif (atual - int(r)) <= 18:
            menor.append(atual - int(r))
            mme = mme + (atual - int(r))
        elif int(r) >> atual or int(r) << 1850:
            print('Idade invalida!')
            exit()
    else:
        print('O valor digitado é invalido!')
        exit()
print('A media das idades do menores é de {}\nA media das idades dos maiores é de {}'.format(mme / len(menor), mma / len(maior))) 

