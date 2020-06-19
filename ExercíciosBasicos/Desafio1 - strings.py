nome = 'Joao Pedro'
idade = 25
altura = 1.70
peso = 80
ano_atual = 2020

imc = peso / (altura **2)
ano_nasc = ano_atual - idade

#Modo 1
print('{0} tem {1} anos, {2} de altura e pesa {3} kg.' .format(nome, idade, altura, peso))
print('O IMC de {0} é {1:.2f}.' .format(nome, imc))
print('{0} nasceu em {1}.' .format(nome, ano_nasc))

#Modo 2
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}.')

