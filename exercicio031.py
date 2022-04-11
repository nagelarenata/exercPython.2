distancia = float(input('Qual é a distância da viagem em Km? '))
menor = distancia * 0.5
maior = distancia * 0.45
if distancia < 200:
    print(f'O preço da passagem é R${menor:.2f}')
else:
    print(f'O preço da passagem é R${maior:.2f}')