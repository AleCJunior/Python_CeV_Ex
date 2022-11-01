#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome: '))
ns = nome.split()
print('Seja bem vindo(a), {} {}'.format((ns[0]),(ns[-1])))
