num = int(input('Digite um número:\n'))
num2 = int(input('Digite um número:\n'))
num3 = int(input('Digite um número:\n'))

menor = num

if num > num2 < num3:
    menor = num2

if num > num3 < num2:
    menor = num3


maior = num

if num < num2 > num3:
    maior = num2

if num < num3 > num2:
    maior = num3

print(f'Maior número {maior}\nMenor número {menor}')
