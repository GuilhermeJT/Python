num = int(input('Número:\n'))
unidade = num % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f'Unidade: {unidade}')
print(f'Dezena : {dezena}')
print(f'Centena: {centena}')
print(f'Milhar : {milhar}')
