#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

gen = str(input('Qual é o seu genero ? \n[ 1 ] HOMEM\n[ 2 ] MULHER\n: '))
if gen.isnumeric():
    if int(gen) > 0 and int(gen) < 3:
        pa = (input('Qual é o seu peso e altura, respectivamente? (Ex: 1.71 65.5)\n: '))
        pa.split()
        if len(pa) == 9 or len(pa) == 10:
            altura = float(pa[0:4])
            peso = float(pa[5:9])
            imc = float(peso / (altura * altura))
            if imc < 18.5:
                print('Seu IMC é de {:.2f}, e você está abaixo do peso ideal!'.format(imc))
            elif 18.5 <= imc < 25:
                print('Seu IMC é de {:.2f}, e você está no peso ideal!'.format(imc))
            elif 25 <= imc < 30:
                print('Seu IMC é de {:.2f}, e você está com sobrepeso!'.format(imc))
            elif 30 <= imc < 40:
                print('Seu IMC é de {:.2f}, e você está na faixa da obesidade!'.format(imc))
            else:
                print('Seu IMC é de {:.2f}, e você está na faixa da obesidade morbida, procure ajuda medica!'.format(imc))
        else:
            print('o valor digitado é invalido')
    else:
        print('o valor digitado é invalido')
else:
    print('O valor digitado é invalido')
