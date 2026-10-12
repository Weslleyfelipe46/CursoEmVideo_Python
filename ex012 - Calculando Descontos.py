#Exercício Python 12: Faça um algoritmo que leia o preço
# de um produto e mostre seu novo preço, com 5% de desconto.

print(25 * '=', 'Calculando Descontos', 25 * '=')
print(end='\n')

produto = float(input('Digite o preço do produto: '))
novo_preco = produto - (produto * 5 / 100)
print(end='\n')

print(f'O produto que custava RS$ {produto}, na promoção com desconto de 5% vai custar RS$ {novo_preco:.2f}.')

print(50 * '=')