num = float(input('Qual o salario do funcionario? R$'))

aumento = num + (num * 15 / 100)

print(f'O funcionario que ganhava {num:.2f}, com aumento de 15%, ganhará {aumento:.2f}')
