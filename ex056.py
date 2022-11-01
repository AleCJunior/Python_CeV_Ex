# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

cont = int(input('Quantas pessoas você quer registrar ?\n: '))  # Valor de pessoas a serem registradas.
mulher = 0  # Contador de quantas mulheres foram registradas.
homem = 0   # Contador de quantos homens foram registrados.
hv = ''    # Registro do homem mais velho.
idm = 0     # Registro de todas as idades somadas.
pessoas_matriz = []     # lista matriz de todas as pessoas registradas, e suas caracteristicas.
for p in range(1, cont + 1):    # Contador de pessoas
    nome = str(input('Registre a {}ª pessoa\nNome: '.format(p)))    # Registro de NOME.
    idade = int(input('Idade: '))   # Registro de IDADE.
    gen = str(input('Genero ? [ M ] ou [ F ]: '))   # Registro de GENERO.
    pessoa = [nome, idade, gen]     # Gerar lista da pessoa.
    pessoas_matriz.append(pessoa)   # Inserir lista da pessoa na lista matriz.
    idm = pessoas_matriz[p - 1][1] + idm    # Somar idade da pessoa registrada, com a idade de todos.
    if pessoas_matriz[p-1][2] == 'F' and pessoas_matriz[p-1][1] << 20:  # Contar mulheres abaixo de 20 anos.
        mulher = + 1
    if pessoas_matriz[p-1][2] == 'M' and pessoas_matriz[p-1][1] >> homem:   # Registrar o homem mais velho.
        homem = pessoas_matriz[p-1][1]
        hv = pessoas_matriz[p-1][0]
print('Idade media entre os {} registrados é de {}'.format(cont, idm / cont))
print('O numero de mulheres acima de 20 anos é {}'.format(mulher))
print('O homem mais velho registrado é o {}'.format(hv))
