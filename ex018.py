from math import radians, sin, cos, tan
ang = int(input('Digite um angulo: '))
cos = cos(radians(ang))
sen = sin(radians(ang))
tan = tan(radians(ang))
print('Sobre o angulo {}\nSeno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}'.format(ang, sen, cos, tan))
