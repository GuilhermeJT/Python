a = float(input('Digite um dos lados:\n'))
b = float(input('Digite o valor do outro lado:\n'))
c = float(input('Digite o valor do outro lado:\n'))

if a < b + c and b < a + c and c < a + b:
    print('São medidas de um triângulo')

else:
    print('Não são medidas de um triângulo')