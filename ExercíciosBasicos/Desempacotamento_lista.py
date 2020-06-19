"""
Desempacotamento de listas em Python
"""

lista = ['João','Carol','Sansão',1,2,3,4,5,6,7,8,9,100]

n1, n2, n3, *outra_lista, ultimo_valor = lista

print(n1, n2, n3, outra_lista, ultimo_valor)
print(n1, n2, n3)
print(outra_lista)
print(ultimo_valor)