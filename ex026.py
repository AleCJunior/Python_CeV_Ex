#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
fr = str(input('Manda o texto ae: '))
if (fr.lower().count('a') > 0):
    print('O texto tem {} Caracteres = A\nPrimeiro: {}\nUltimo: {}'.format(fr.lower().count('a'),(fr.lower().find('a')),(fr.lower().rfind('a')+1)))
else:
    print('O texto não tem caracteres = A')