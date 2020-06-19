"""
Invertendo valores de variáveis em Python
"""

x = 10
y = 'João'

#Em outras linguagens de programação
"""
z = x
x = y
y = z
"""

#Em Python
x, y = y, x

#Funciona para mais que 2 variáveis
#x, y, z = z, x, y

print(f'x = {x} e y = {y}')