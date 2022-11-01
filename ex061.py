# Exercício Python 61 Refaça o DESAFIO 51, lendo o primeiro termo e a razão de
# uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

entry = input('Digite quantos calculos você quer fazer, em seguida o termo e, após, a razão.\nEx: "10 5 2"\n: ')

while (entry.replace(' ', '')).isnumeric() is False or int(len(entry.split())) != 3:
    entry = input('Dados invalidos! tente novamente: ')
es = entry.split()

q = int(es[0])
t = int(es[1])
r = int(es[2])
c = 0

while q != 1:
    print((c * r) + t, end=' -> ')
    q = q - 1
    c = c + 1
print((c * r) + t)
