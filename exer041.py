from datetime import date

anoAtual = date.today().year

nascimento = int(input('Qual ano você nasceu:\n'))

anos = anoAtual - nascimento

if anos <= 9:
    print(f'Você tem {anos} anos e é categoria MIRIM')

elif 9 < anos <= 14:
    print(f'Você tem {anos} anos e é categoria INFANTIL')

elif 14 < anos <= 19:
    print(f'Você tem {anos} anos e é categoria JUNIOR')

elif 19 < anos <= 25:
    print(f'Você tem {anos} anos e é categoria SÊNIOR ')

elif anos > 25:
    print(f'Você tem {anos} anos e é categoria MASTER')