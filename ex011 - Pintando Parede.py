# Exercício Python 11: Faça um programa que leia a largura 
# e a altura de uma parede em metros, calcule a sua área e 
# a quantidade de tinta necessária para pintá-la, sabendo 
# que cada litro de tinta pinta uma área de 2 metros quadrados.


print(25 * '=', 'Pintando Parede', 25 * '=')
print(end='\n')

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura

print(f'Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}m²\n') 

tinta = area / 2

print(f'Você vai precisar de {tinta}l de tinta, para pinta sua parede.\n')
print(25 * '=','', 25 * '=')