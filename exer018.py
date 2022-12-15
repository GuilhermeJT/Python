import math
an = float(input('Digite o angulo que você deseja:'))
seno = math.sin(math.radians(an))
print(f'O angulo {an} tem o seno de {seno:.2f}')
cos = math.cos(math.radians(an))
print(f'O Cosseno desse angulo é {cos:.2f}')
tan = math.tan(math.radians(an))
print(f'tan {tan:.2f}')
