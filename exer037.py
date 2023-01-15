num = int(input('Digite um número:\n'))
print('''Escolha uma base de conversão:
1 - BINÁRIO
2 - OCTAL
3 - HEXADECIMAL''')

opcao = int(input())

if opcao == 1:
    print(f'{bin(num)[2:]}')

elif opcao == 2:
    print(f'{oct(num)[2:]}')

elif opcao == 3:
    print(f'{hex(num)[2:]}')

else:
    print('ERRO!! VOCê DIGITOU UM NÚMERO DIFERENTE DE 1,2,3')
