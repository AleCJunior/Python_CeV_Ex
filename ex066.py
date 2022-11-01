# Exercício Python 66. Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, sendo a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre elas (desconsiderando o flag).

soma = cont = 0


def validate():
    global num
    while num.isnumeric() is False or int(len(num.split())) != 1:
        if num.isnumeric() is False:
            num = input('Valor digitado é invalido! tente novamente: ')
        elif int(len(num.split())) != 1:
            num = input('Apenas um valor por vez! tente novamente: ')


while True:
    if cont == 0:
        num = input('Digite varios valores. a hora que quiser parar, digite "999"\n: ')
        validate()
        if num == '999':
            print('Você ainda não digitou nenhum valor...\nAté a proxima.')
            exit()

    else:
        num = input('Digite outro valor: ')
        validate()
    if num == '999':
        break
    else:
        soma = soma + int(num)
        cont = cont + 1
print(f'A soma dos {cont} numeros digitados é igual a {soma}')
