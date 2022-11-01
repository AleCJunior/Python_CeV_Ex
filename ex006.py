n = input('\033[1;97;40m Digite um numero: \033[m\n')
if n.isnumeric():
    print('\033[1;97;40mO valor em dobro é:\033[1;32;40m {} \033[m\n\033[1;97;40mEm triplo:\033[1;32;40m {} \033[m\n\033[1;97;40mE a raiz quadrada:\033[1;32;40m {:.3f} \033[m'.format(int(n)*2, int(n)*3, int(n)**(1/2)))
else:
    print('\033[1;30;41m Leia direito!! \033[1;31;40m {} \033[1;30;41m não é um numero! \033[m'.format(n))