'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual sua peso: '))
altura = float(input('Qual sua altura: '))

imc = peso / (altura ** 2)

print(f'Seu imc é {imc:.1f}')

if imc < 18.5:
    print('ABAIXO DO PESO!')

elif imc < 25:
    print('PESO IDEAL!')

elif imc < 30:
    print('SOBREPESO!')

elif imc < 40:
    print('OBESIDADE!')

elif imc > 40:
    print('OBESIDADE MÓRBITA')


 