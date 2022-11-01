# Exercício Python 69. Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print('Bem vindo ao sistema de cadastro!')

modo = input('Deseja operar em qual modo ?\n[ 0 ] SIMPLES\n[ 1 ] COMPLICADO\n: ')
while modo.isnumeric() is False or int(len(modo.split())) != 1:
    modo = input('Valor invalido! tente novamente: ')

if int(modo) == 0:
    a1 = a2 = a3 = 0
    while True:
        yo = int(input('IDADE?: '))
        ge = str(input('GENERO?: '))
        keep = str(input('DESEJA CONTINUAR? [S/N]: '))
        if keep == 'S':
            if yo > 18:
                a1 = a1 + 1
            if ge == 'M':
                a2 = a2 + 1
            if ge == 'F' and yo < 20:
                a3 = a3 + 1
        else:
            print(f'Maiores de 18: {a1}\nHomens registrados: {a2}\nMulheres com menos de 20 anos: {a3}')
            break


else:
    ficha = []
    matriz_pessoas = []
    c1 = c2 = c3 = a = b = c = 0


    def registros():
        global ficha, matriz_pessoas
        while True:
            nome = input('Digite seu primeiro nome: ')
            while int(len(nome.split())) != 1 or nome.isalpha() is False:
                nome = input('Entrada de nome invalida! tente novamente: ')
            ficha.append(nome)

            # --------------------------------------------------------------------------------------------------------------

            idade = input('Digite sua idade: ')
            while int(len(idade.split())) != 1 or idade.isnumeric() is False:
                idade = input('Entrada de idade invalida! tente novamente: ')
            ficha.append(idade)

            # --------------------------------------------------------------------------------------------------------------

            gen = input('Digite seu genero [ M / F ]: ')
            while gen.lower() != 'm' and gen.lower() != 'f':
                gen = input('Entrada de genero invalida! tente novamente: ')
            ficha.append(gen.upper())

            # --------------------------------------------------------------------------------------------------------------

            matriz_pessoas.append(ficha)
            ficha = []

            # --------------------------------------------------------------------------------------------------------------

            continuar = input('Deseja continuar a registrar ? [ S / N ]: ')
            while continuar.lower() != 's' and continuar.lower() != 'n':
                continuar = input('Resposta invalida! tente novamente: ')
            if continuar.lower() == 'n':
                relatorio()
                break

            # --------------------------------------------------------------------------------------------------------------


    def relatorio():
        global c1, c2, c3, a, b, c

        # ------------------------------------------------------------------------------------------------------------------

        while c < int(len(matriz_pessoas)):
            if matriz_pessoas[c][2] == 'F':
                if int(matriz_pessoas[c][1]) < 20:
                    c3 = c3 + 1
                elif int(matriz_pessoas[c][1]) > 18:
                    c1 = c1 + 1
            else:
                if int(matriz_pessoas[c][1]) > 18:
                    c1 = c1 + 1
                c2 = c2 + 1
            c = c + 1

        print(f'Pessoas com mais de 18 anos: {c1}')
        print(f'Homens registrados: {c2}')
        print(f'Mulheres com menos de 20 anos: {c3}')


    registros()
