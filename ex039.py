# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu ?\n'))
idade = atual - nasc
if idade > 18:
    print('ATENÇÃO! Você deveria ter se alistado em {}, a {} ano(s) atrás.'.format((atual - (idade - 18)), (idade - 18)))
elif idade < 18:
    print('ATENÇÃO! Você terá que se alistar em {}, daqui a {} ano(s)'.format((atual - (idade - 18)), (18 - idade)))
else:
    print('Jovem, está no ano de se alistar, procure a unidade mais proxima.')
