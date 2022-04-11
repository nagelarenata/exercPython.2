print('*' * 50)
print(' S O M A  P R O G R E S S A O  G E O M E T R I C A   ')
print('*' * 50)
a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
a10 = a1 + (9 * r)
soma = 0
for c in range(a1, a10, r):
    soma = soma + c
print(f' A soma dos 10 primeiros termos é {soma}')