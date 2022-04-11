#soma apenas dos números pares
c = 0
soma = 0
while c < 6:
    n1 = int(input('Escolha um número: '))
    c = c + 1
    if n1 % 2 == 0:
        soma = soma + n1
print(f'A soma é {soma}')