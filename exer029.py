velo = int(input('Velocidade atual do carro:\n'))

if velo < 81:
    print('Velocidade aceitavel')
    print('Tome cuidado!!')

else:
    dife = velo - 80
    valor = dife * 7

    print(f'!! EXCESSO DE VELOCIDADE !!')
    print(f'Você foi multado em {valor}')

    