frase = str(input('Digite uma frase:\n')).strip()
frase = frase.upper()

print(f'apareceu {frase.count("A")} a letra A')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}') #coloca o +1 pq o codigo começa a contar do 0
print(f'A Ultima letra A apareceu na posição {frase.rfind("A")+1}') #rfind começa a caçar do lado direito right
