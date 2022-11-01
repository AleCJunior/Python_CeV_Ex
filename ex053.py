# Exercício Python 53. Crie um programa que leia uma frase qualquer e diga se
# ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input('Digite uma frase, direi se é um palindromo.\n: '))
fsl = frase.lower()
fs = (fsl.replace(' ', ''))
frasel = fs.lower()
fsv = str()
contfsl = int(len(fsl))
for c in range (0, len(fsl)):
    contfsl = contfsl - 1
    fsv = fsv + fsl[contfsl]
print('Normal: {}\nInvertido: {}'.format(fsl, fsv))
print('Sem espaços:\n{}\n{}'.format(fsl.replace(' ', ''), fsv.replace(' ', '')))
fsvc = fsv.replace(' ', '')
if frasel == fsvc:
    print('É um palindromo')
else:
    print('Não é um palindromo')
#SIM, EU ASSISTI A AULA DEPOIS DE FAZER O EXERCICIO POR CONTA PROPRIA, EU VI AS DICAS.
