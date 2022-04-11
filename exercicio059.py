from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

x = 1
resultado = 0
while x != 5:
    x = int(input('''Opções:
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa
        .....: '''))
    if x == 1:
        resultado = n1 + n2
        print(f'{n1} + {n2} = {resultado}'))
    elif x == 2:
        resultado = n1 * n2
        print(f'{n1} x {n2} = {resultado}'))
    elif x == 3:
        if n1 > n2:
            print(f'O maior é {n1}')
        else:
            print(f'O maior é {n2}')
    elif x == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite um novo número: '))
    elif x == 5:
        print('Encerrando...')
        sleep(2)
        print('Programa encerrado, valeu por utilizar!')
    else:
        print('Inválido, tente novamente!')