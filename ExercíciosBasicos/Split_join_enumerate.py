"""
Split, Join, Enumerate em Python
* Split - Dividir uma string #str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista #list / iteráveis
"""

string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

"""
#Contar quantas vezes a palavra apareceu na frase.
for valor in lista_1:
    print(f'A palavra "{valor}" apareceu {lista_1.count(valor)}x na frase.')
"""

"""
#Contar qual palavra apareceu mais vezes na frase.
palavra = ''
contagem = 0

for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')
"""

"""
#Exemplo para tratar a frase
for valor in lista_2:
    print(valor.strip().capitalize())
"""

string_2 = 'O Brasil é penta'
lista_3 = string_2.split(' ')
string_3 = ' '.join(lista_3)
string_4 = ','.join(lista_3)

"""
#Prints para ver o join
print(string_2)
print(lista_3)
print(string_3)
print(string_4)
"""

#Enumerate - coloca os índices nos itens da lista
for indice, valor in enumerate(lista_3):
    print(indice, valor)