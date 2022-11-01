# 035: Desenvolva um programa que leia o comprimento de três
# retas e diga ao usuário se elas podem ou não formar um triângulo.
r = str(input('Digite o valor inteiro de 3 retas, em sequencia\n: '))
l = r.split()
v = str('Dá pra fazer um triangulo')
f = str('Não dá pra fazer um triangulo')
if int(l[0]+l[1]) != int(l[2]):
    if int(l[0]+l[1]) << int(l[2]):
        print(v)
    else:
        print(f)
else:
    print(f)
