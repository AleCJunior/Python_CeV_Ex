# Exercício Python 65. Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

mal = []
mel = []
nm = []
nl = []
md = 0
mm = []
cvn = 0
cc = 0
c1 = 0
c2 = 0
maior = menor = mat = met = 0


def val_numeros():
    global nl, nm, cvn, md, cc, c1, maior, menor, mat, met
    md = c1 = 0
    if cc == 0:
        numeros = input('Digite varios numeros, para serem processados. Minimo de 2 valores.\nEx: "10 20 30 40 50"\n: ')
    else:
        numeros = input('Digite outros valores: ')
    while (numeros.replace(' ', '')).isnumeric() is False or int(len(numeros.split())) < 2 or (numeros in '-') is True:
        if (numeros in '-') is True:
            numeros = input('Valores negativos não são permitidos! tente novamente: ')
        else:
            numeros = input('Entrada de dados invalida! tente novamente: ')
    nl = numeros.split()
    while c1 <= int(len(nl)) - 1:
        if c1 == 0:
            maior = menor = int(nl[c1])
        else:
            if int(nl[c1]) > maior:
                maior = int(nl[c1])
            elif int(nl[c1]) < menor:
                menor = int(nl[c1])
        md = md + int(nl[c1])
        c1 = c1 + 1
    mal.append(maior)
    mel.append(menor)
    md = md / int(len(nl))
    print(f'A media dos numeros digitados é de {md}.\nMaior numero = {maior}.\nMenor numero = {menor}.')
    nm.append(nl)
    mm.append(md)
    if cc == 0:
        mat = maior
        met = menor
    else:
        if maior > mat:
            mat = maior
        if menor < met:
            met = menor
    continuar()


def continuar():
    global nl, nm, cc, c2
    cc = c2 = 0
    cc = cc + 1
    stop = input('Deseja continuar a digitar numeros ? [ S / N ]: ')
    while (stop in 'SsNn') is False:
        stop = input('Resposta invalida, tente novamente: ')
    if stop.upper() == 'S':
        val_numeros()
        nm.append(nl)
        continuar()
    else:
        print('Relatorio total')
        while c2 < int(len(mm)):
            print(f'{nm[c2][:]} -media-> {mm[c2]} / maior -> {mal[c2]} / menor -> {mel[c2]}')
            c2 = c2 + 1
        print(f'Maior e menor numero entre todos os numeros: {mat} e {met}')
        print('Fim')
        exit()


val_numeros()
