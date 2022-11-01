#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a
# soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

valores = []
soma = 0
valor = int(0)
for c in range(0, 6):
    valor = input('Insira um valor: ')
    valores.append(valor)
    if (int(valores[c]) % 2) == 0:
        soma += int(valores[c])
print('A soma dos valores pares é de {}'.format(soma))
