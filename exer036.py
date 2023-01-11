casa = float(input('Qual o valor da casa:\n'))
salario = float(input('Qual o valor do seu salário:\n'))
anos = int(input('Em quantos anos você vai pagar:\n'))

por = salario * 30 / 100
prestacao = casa / (anos * 12)

if prestacao > por:
    print('EMPRESTIMO NEGADO')

else:
    print('EMPRESTIMO APROVADOO!!')