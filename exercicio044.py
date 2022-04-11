while True:
    print('=-' * 25)
    print(' G E R E N C I A D O R  D E  P A G A M E N T O S  ')
    print('=-' * 25)
    valor = float(input('Qual é o valor do móvel que você deseja comprar? R$'))
    metodo = int(input('''Qual será o método de pagamento?
                   [ 1 ] á vista no dinheiro ou cheque
                   [ 2 ] à vista no cartão
                   [ 3 ] em até 2 vezes no cartão
                   [ 4 ] em 3 vezes ou mais no cartão
    '''))
    if metodo == 1:
        print('Esse método oferece 10% de desconto')
        vf = valor * 0.9
        d = valor * 0.1
        print(f'À vista, o móvel custa R${vf:.2f} e possui R${d:.2f} de desconto!')
    elif metodo == 2:
        print('Esse método oferece 5% de desconto')
        vf = valor * 0.95
        d = valor * 0.05
        print(f'À vista, o móvel custa R${vf:.2f} e possui R${d:.2f} de desconto!')
    elif metodo == 3:
        print('Esse método não oferece desconto.')
        parc = valor / 2
        print(f'O valor total a ser pago é R${valor:.2f} e as parcelas são de R${parc:.2f}')
    else:
        nparc = int(input('Em quantas vezes você deseja fazer? '))
        parc = (valor * 1.2) / nparc
        print(f'Esse método de pagamento possui 20% de juros. Você pagará {nparc} parcelas de R${parc:.2f}.')
        print(f'O valor total será {valor * 1.2 :.2f}')
    c = int(input('''Deseja fazer uma nova simulação? 
    [ 1 ] SIM
    [ 2 ] NÃO
    '''))
    if c == 2:
        break
print('Volte sempre!')