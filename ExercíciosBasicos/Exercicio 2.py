"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Informe um horario (0-23): ')

try:
    horario = int(horario)

    if horario < 0 or horario > 23:
         print("Horário deve estar entre 0 e 23")
    else:
        if horario <= 11:
            print('Boa dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
except:
    print(f'{horario} não é uma hora valida.')