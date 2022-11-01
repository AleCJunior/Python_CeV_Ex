#crie um programa que leia o nome completo de uma pessoa e mostre:
# uppercase, lowercase, total len (sem espaço), e len do primeiro nome
nome = str(input('Digite seu nome: '))
print(nome.upper())
print(nome.lower())
print((nome.replace(' ','')),': ',(len(nome.replace(' ',''))))
nomesplit = nome.split()
print((nomesplit[0]),': ',(len(nomesplit[0])))
