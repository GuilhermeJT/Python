import random
import time

numeros = [0,1,2,3,4,5]

num = int(input('tente adivinhar um número entre 0 e 5...\n'))
numAle = random.choice(numeros)

if 0 < num < 6:
    print('PROCESSANDO...')
    time.sleep(1)
    if num == numAle:
        print(f'Parabéns você acertou o número!!!')
        
    else:
        print(':( você errou o número')

else:

    print('Você digitou um número menor de 0 e maior que 1')