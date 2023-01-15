a = float(input('Digite um dos lados:\n'))
b = float(input('Digite o valor do outro lado:\n'))
c = float(input('Digite o valor do outro lado:\n'))

if a < b + c and b < a + c and c < a + b:
    print('\033[34mSão medidas de um triângulo')

else:
    print('\033[34mNão são medidas de um triângulo')
