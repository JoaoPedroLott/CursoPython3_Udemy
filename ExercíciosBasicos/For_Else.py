"""
For / Else em Python
"""

lista = ['Carol','João','Sansão']

"""
#Percorre a lista e imprime todos os valores dela

for valor in lista:
    print(valor)
"""

for valor in lista:
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J.')