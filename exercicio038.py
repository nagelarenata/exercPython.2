n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
elif n2 == n1:
    print(f'Os números digitados são iguais')
else:
    print('Opção inválida. Tente novamente.')
