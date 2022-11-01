user = input('digite seu usuario: ')
c = {
    'ngpb':'\033[1;30;107m',
    'limpa':'\033[m'
}
print('{}Seja bem vindo, {} {}'.format(c['ngpb'], user, c['limpa']))
