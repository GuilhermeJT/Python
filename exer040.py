nota = float(input('Primeira nota:\n'))
nota2 = float(input('Segunda nota:\n'))

media = (nota + nota2) / 2

if media < 5:
    print('VOCÊ FOI REPROVADO!!')

elif 5 < media < 6.9:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO')

elif media >= 7:
    print('PARABÉNS!! VOCÊ ESTÁ APROVADO!!') 

print(f'Sua média é {media}')