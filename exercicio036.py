print('--------------------------------------')
print('M I N H A  C A S A  M I N H A  V I D A')
print('--------------------------------------')
valor = float(input('Quanto custa a casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = float(input('Em quantos anos o empréstimo será pago? '))
meses = 12 * anos
prestacao = valor / meses
percentual = 0.3 * salario
if prestacao > percentual:
    print(f'Empréstimo negado! A parcela ficaria {prestacao:.2f}, valor que supera 30% do salário.')
else:
    print(f'Empréstimo aprovado! Parabéns, sua parcela será de {prestacao:.2f}!')
