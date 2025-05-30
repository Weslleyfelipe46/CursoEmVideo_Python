print(20 * '=', 'Desafio 004', 20 * '=')
print('Faça um programa que leia algo pelo teclado e mostre na \ntela o seu tipo primitivo e todas as informações possiveis!')
print()

leia = input('Digite algo: ')

print(f'O tipo primitivo é {type(leia)}')
print(f'O {leia} é um número? {leia.isnumeric()}')
print(f'O {leia} é alfabetico? {leia.isalpha()}')
print(f'O {leia} está em Caxa Alta? {leia.isupper()} ')
print(f'O {leia} está capitalizada? {leia.islower()} ')
