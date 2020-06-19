"""
Operador ternário em Python
"""

logged_user = False

"""
if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'
"""

msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg)

"""
idade = 18

if idade >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar.')
"""

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números.')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg2 = 'Pode acessar.' if e_de_maior else 'Não pode acessar.'

    print(msg2)