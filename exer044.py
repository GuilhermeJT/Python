'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

print(f'{"LOJA ONLINE":=^30}')
valor = float(input('Qual o valor do produto: '))
print('Será pago : ')
print('[ 1 ] Á VISTA')
print('[ 2 ] Á VISTA NO CARTÃO')
print('[ 3 ] EM ATÉ 2X NO CARTÃO')
print('[ 4 ] EM 3X OU MAIS NO CARTÃO')
print(30 * '=')
opcao = int(input('Qual opção: '))

match opcao:
    case 1:
        des = (valor * 10) / 100
        valorFinal = valor - des
            
    case 2:
        des = (valor * 5) / 100
        valorFinal = valor - des

    case 3:
        valorFinal = valor

    case 4:
        juros = (valor * 20) / 100
        valorFinal = valor + juros

print(f'Valor final ficou de R${valorFinal}')

