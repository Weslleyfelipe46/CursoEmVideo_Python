#Exercício Python 13: 
# Faça um algoritmo que leia o salário de um funcionário e 
# mostre seu novo salário, com 15% de aumento.

print(25 * '=', 'Reajuste Salarial', 25 * '=')
print(end='\n')

salario = float(input('Digite seu salário: '))
print(end='\n')

novo_salario = salario + (salario * 15 / 100)

print(f'Seu salário antigo era RS$ {salario}, com o aumento de 15% ficou RS$ {novo_salario}')

print(end='\n')
print(50 * '=')