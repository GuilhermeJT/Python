cidade = str(input('Qual cidade você nasceu?\n')).strip() #strip é para tirar os espaços inuteis 
cidade = cidade.upper()

if(cidade[0:5] == 'SANTO'):
    print('A cidade que você nasceu começa com "Santo"')

else:
    print('A cidade que você nasceu não começa com "Santo"')



