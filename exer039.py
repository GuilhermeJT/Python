from datetime import date
data = int(input('Qual seu ano de nascimento?? '))
anoAtual = date.today().year

anos = anoAtual - data
faltaMaior = anos - 18
faltaMenor = 18 - anos
alistamento = anoAtual + faltaMenor
alistamentoATrasado = anoAtual - faltaMaior
if anos < 18:

    print(f'Você tem {anos}')
    print(f'Falta {faltaMenor} anos para o alistamento')
    print(f'Seu alistamento sera {alistamento} ')

elif anos == 18:
    
    print('Seu alistamento é esse Ano')

else:
    print(f'Você tem {anos}')
    print(f'Você ta com o alistamento atrasado')
    print(f'O ano que você deveria ter se alistado é {alistamentoATrasado}')


    