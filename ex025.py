#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite seu nome: '))
if ('silva' in nome.lower()):
    print('Tem Silva sim! kkkpobre.')
else:
    print('Não tem Silva não.')
