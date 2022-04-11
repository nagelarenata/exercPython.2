L1 = float(input('L1: '))
L2 = float(input('L2: '))
L3 = float(input('L3: '))
if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo')
