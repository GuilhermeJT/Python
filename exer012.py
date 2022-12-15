num = float(input('Digite o valor do produto: R$'))

des = (num * 5) / 100
total = num - des

print(f'O valor R${num:.2f} com desconto de 5% fica {total:.2f}')
