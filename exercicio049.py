#tabuada - usuario escolhe
n = int(input('Quer calcular a tabuada de qual número? '))
for c in range(0, 11):
    tab = n * c
    print(f'{n} x {c} = {tab}')