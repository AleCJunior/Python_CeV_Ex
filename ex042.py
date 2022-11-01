#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

vt = str(input('Digite o valor dos 3 lados do triangulo, em sequencia:\n '))
vs = vt.split()
v1 = int(vs[0])
v2 = int(vs[1])
v3 = int(vs[2])
v = str('forma um triangulo')
if v1 << v2 + v3 and v2 << v1 + v3 and v3 << v1  + v2:
    if v1 == v2 == v3:
        print(v, 'de classe EQUILATERO')
    elif v1 == v2 or v1 == v3:
        print(v, 'de classe ISÓSCELES')
    else:
        print(v, 'de classe ESCALENO')
else:
    print('Não dá pra fazer um triangulo')
