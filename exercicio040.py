print('------------------------------------')
print('  E S C O L A  M O N T E S S O R I  ')
print('------------------------------------')
# cada prova da escola vale 10
n1 = float(input('Digite a nota da sua primeira avaliação: '))
n2 = float(input('Digite a nota da sua segunda avaliação: '))
n3 = float(input('Digite a nota da sua terceira avaliação: '))
nf = (n1 + n2 + n3)/3
if nf < 5:
    print(f'Sua média final é {nf:.1f}. Você está reprovado e não possui direito a prova de recuperação.')
elif nf >= 5 and nf <= 6.9:
    print(f'Sua média final é {nf:.1f}. Você está de recuperação.')
else:
    print(f'Parabéns! Você passou direto. Sua média final é {nf:.1f}')
