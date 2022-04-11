from random import randint
while True:
    print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    itens = ['Pedra', 'Papel', 'Tesoura']
    sorteio = randint(0, 2)
    opcao = int(input('Escolha o número da sua jogada: '))
    print('=' * 28)
    print(f'O computador jogou {itens[sorteio]}')
    print(f'Você jogou {itens[opcao]}')
    if itens[sorteio] == itens[opcao]:
        print('O jogo empatou. Tente novamente.')
    elif opcao == 2 and sorteio == 0:
        print('Parabéns, você ganhou!')
    elif opcao == 0 and sorteio == 2:
        print('Parabéns, você ganhou!')
    elif opcao == 1 and sorteio == 0:
        print('Parabéns, você ganhou!')
    else:
        print('Que pena, você perdeu. Tente novamente.')
    r = int(input('''Deseja jogar novamente?
    [ 0 ] SIM
    [ 1 ] NÃO
    '''))
    if r == 1:
        break
