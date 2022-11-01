import random
import math
print('Para sortear os 4 alunos, digite o nome deles abaixo, e pressione enter')
a = str(input(''))
b = str(input(''))
c = str(input(''))
d = str(input(''))
weight_dict = {
    a: 1,
    b: 2,
    c: 3,
    d: 4,
} #Sim, eu pesquisei na internet, tudo que foi usado de random
print('E o sorteado ééééé:\n{}'.format(random.choice(list(weight_dict))))

