# Exercício Python 62. Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

entry = input('Digite quantos calculos você quer fazer, em seguida o termo e, após, a razão.\nEx: "10 5 2"\n: ')

while (entry.replace(' ', '')).isnumeric() is False or int(len(entry.split())) != 3:
    entry = input('Dados invalidos! tente novamente: ')
es = entry.split()

q = int(es[0])
t = int(es[1])
r = int(es[2])
c = 0
tot = []
lista = []


def mypa():
    global q, t, r, c, tot
    while q != 1:
        print((c * r) + t, end=' -> ')
        q = q - 1
        c = c + 1
        lista.append((c * r) + t)
    print((c * r) + t, '-> PAUSA')
    lista.append((c * r) + t)
    cont = input('Você deseja continuar ? Se sim, digite quantas progressões a mais quer fazer. Se não, digite "0"\n: ')

    while cont.isnumeric() is False or int(len(cont.split())) != 1:
        cont = input('Dados invalidos! tente novamente: ')

    if int(cont) != 0:
        tot.append(lista)
        c = c + 1
        q = int(cont)
        mypa()

    else:
        print('Fim da PA!')


mypa()
