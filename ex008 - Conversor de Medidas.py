print(25 * '=', 'Conversor de Medidas', 25 * '=')

medida = float(input('Digite uma medida em metro: '))


kilometros = (medida * 1000)/1000000
hectometros = (medida * 100)/10000
decametros = (medida * 10)/100
decimetros = medida * 10
centimetros = medida * 100
milimetros = medida * 1000

print(f'A medida digitada foi {medida:.2f}m, vou converter ela pra você! ')
print(f'é igual a {kilometros:.3f}km.')
print(f'é igual a {hectometros:.2f}hm.')
print(f'é igual a {decametros:.1f}dam.')
print(f'é igual a {decimetros:.0f}dm.')
print(f'é igual a {centimetros:.0f} centimetros.')
print(f'é igual a {milimetros:.0f} milimetros.')
