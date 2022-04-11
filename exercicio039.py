from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano
if idade > 18:
    y = idade - 18
    print(f'Você deve/deveria ter se alistado há {y} anos.')
elif idade == 18:
    print('Esse é o ano em que você precisa se alistar.')
else:
    x = 18 - idade
    print(f'Você deverá se alistar daqui há {x} anos.')
