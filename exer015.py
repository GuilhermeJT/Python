dias = int(input('Por quantos dias você alugou o carro:'))
km = float(input('Quantos km percorreu:'))

preço_dia = dias * 60
km_rodado = km * 0.15
total = preço_dia + km_rodado

print(f'Total a pagar é de R${total:.2f}')
