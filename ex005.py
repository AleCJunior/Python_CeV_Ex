#Crie um programa que leia um numero e diga seu sucessor e seu antecessor!
n = input('\033[1;97;40m Digite um numero: \033[m\n')
if n.isnumeric():
    print('\033[1;97;40m O antecessor e o sucessor são, respectivamente: \033[1;34;40m{}\033[1;97;40m e \033[1;34;40m{} \033[m'.format((int(n) - 1), (int(n) + 1)))
else:
    print('\033[1;30;41m Leia direito!! \033[1;31;40m {} \033[1;30;41m não é um numero! \033[m'.format(n))
