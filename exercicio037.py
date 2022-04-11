# conversor numerico #

n = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções para conversão: 
      [1] Binário
      [2] Hexadecimal
      [3] Octal''')
opcao = int(input('Digite sua escolha: '))
if opcao == 1:
    print(f'Em binário, {n} é representado como {bin(n)[2:]}')
elif opcao == 2:
    print(f'Em hexadecimal, {n} é representado como {hex(n)[2:]}')
elif opcao == 3:
    print(f'Em octal, {n} é representado como {oct(n)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
