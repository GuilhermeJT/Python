import time
num = int(input('Digite o primeiro número:\n'))
num2 = int(input('Digite o segundo número:\n'))

print('ANALISANDO!!')
time.sleep(0.5)

if num == num2:
    print('Os números são iguais!!')
elif num > num2:
    print('O primeiro número é MAIOR!!')

else:
    print('O segundo número é MAIOR!!')

