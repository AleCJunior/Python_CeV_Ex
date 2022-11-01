#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cida = str(input('Digite o nome da sua cidade: '))
cidasplit = cida.split()
if ('Santa' in cidasplit[0]):
    print('Sim, começa com Santa')
else:
    print('Não começa com santa não')
