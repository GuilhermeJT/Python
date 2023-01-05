salario = float(input('Qual seu salário atual:\n'))

if salario > 1250:
    final = salario + (10 * salario / 100)
    
else:
    final = salario + (15 * salario / 100)

print(final)