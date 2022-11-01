c = {
    'npb': '\033[1;30;107m',
    'bp': '\033[1;97;40m',
    'c': '\033[m'
}
n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
v1 = n1 + n2

print('A soma entre {}{}{} e {}{}{} resulta em {}{}{}'.format((c['bp']),(n1),(c['c']),(c['bp']),(n2),(c['c']),(c['bp']),(v1),(c['c'])))
