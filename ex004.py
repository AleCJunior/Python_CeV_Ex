
v = str(input('\033[1;97;40mDigite algo:\033[m\n'))
if v.isalnum():
    print('\033[1;30;42m É alfanumerico \033[m\n')
else:
    print('\033[1;30;41m Não é alfanumerico \033[m\n')
#-------------------------------------------------------------
if v.isalpha():
    print('\033[1;30;42m É alfabetico \033[m\n')
else:
    print('\033[1;30;41m Não é alfabetico \033[m\n')
#-------------------------------------------------------------
if v.isascii():
    print('\033[1;30;42m É ascii \033[m\n')
else:
    print('\033[1;30;41m Não é ascii \033[m\n')
#-------------------------------------------------------------
if v.isdigit():
    print('\033[1;30;42m É digito \033[m\n')
else:
    print('\033[1;30;41m Não é digito \033[m\n')
#-------------------------------------------------------------
if v.islower():
    print('\033[1;30;42m É minusculo \033[m\n')
else:
    print('\033[1;30;41m Não é minusculo \033[m\n')
#-------------------------------------------------------------
if v.isdecimal():
    print('\033[1;30;42m É decimal \033[m\n')
else:
    print('\033[1;30;41m Não é decimal \033[m\n')
#-------------------------------------------------------------
if v.isidentifier():
    print('\033[1;30;42m É um identificador \033[m\n')
else:
    print('\033[1;30;41m Não é um identificador \033[m\n')
#-------------------------------------------------------------
if v.isnumeric():
    print('\033[1;30;42m É numerico \033[m\n')
else:
    print('\033[1;30;41m Não é numerico \033[m\n')
#-------------------------------------------------------------
if v.isprintable():
    print('\033[1;30;42m É imprimivel \033[m\n')
else:
    print('\033[1;30;41m Não é imprimivel \033[m\n')
#-------------------------------------------------------------
if v.isspace():
    print('\033[1;30;42m É um espaço \033[m\n')
else:
    print('\033[1;30;41m Não é um espaço \033[m\n')
#-------------------------------------------------------------
if v.istitle():
    print('\033[1;30;42m É titulo \033[m\n')
else:
    print('\033[1;30;41m Não é titulo \033[m\n')
#-------------------------------------------------------------
if v.isupper():
    print('\033[1;30;42m É em maiuscula \033[m\n')
else:
    print('\033[1;30;41m Não é em maiuscula \033[m\n')
