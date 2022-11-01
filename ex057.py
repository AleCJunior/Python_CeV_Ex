# Exercício Python 57: faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
gen = input('Informe seu genero. [M] / [F]\n: ').strip().upper()[0]
while gen not in 'MF':  # Laço para valor invalido
    gen = input('Dados invalidos! tente novamente: ').strip().upper()[0]
print('Genero {} registrado com sucesso!'.format(gen))
