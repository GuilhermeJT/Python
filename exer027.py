nome = str(input('Digite seu nome completo:\n'))

nomes = nome.split()

print(f'Seu primeiro nome: {nomes[0]}')
print(f'Ultimo nome: {nomes[len(nomes)-1]}')
