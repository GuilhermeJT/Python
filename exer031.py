distancia = int(input('Qual a distância da sua viagem?\n'))

if distancia <= 200:
    preco = distancia * 0.50
    print(f'O valor da passagem é de {preco}')

else:
    preco = distancia * 0.45
    print(f'O valor da passagem é de R${preco}')

