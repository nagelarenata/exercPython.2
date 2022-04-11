ano = int(input('Digite um ano: '))
div = ano % 4
if div==0:
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é bissexto')
