#Faça um programa que calcule a soma entre todos os números que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
valor = int(0)
for c in range (3, 501, 3):
    soma += c
    cont += 1
print('A soma de todos os {} valores é de {}'.format(cont, soma))
