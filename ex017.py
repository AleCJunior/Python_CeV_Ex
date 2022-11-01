import math
co = float(input('Valor do Cateto Oposto: '))
ca = float(input('valor do Cateto Adjascente: '))
#hip = ((co**2+ca**2)**0.5)
#hip = (math.sqrt(co**2+ca**2))
hip = math.hypot(co, ca)
print('Valor da hipotenusa: {:.3f}'.format(hip))
