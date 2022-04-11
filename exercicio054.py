from datetime import date
cmenor = 0
cmaior = 0
anohj = date.today().year
for contagem in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da pessoa {contagem}: '))
    if anohj - ano >= 18:
        cmaior += 1
    else:
        cmenor += 1
print(f'Há um total de {cmaior} pessoas maiores de idade e {cmenor} pessoas menores de idade.')