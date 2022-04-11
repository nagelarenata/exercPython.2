sal=float(input('Qual é o seu salário? R$'))
if sal > 1250.00:
    print(f'Você terá um aumento de R${sal * 0.1:.2f} e passará a receber R${sal * 1.1:.2f}')
else:
    print(f'Você terá um aumento de R${sal * 0.15:.2f} e passará a receber R${sal * 1.15:.2f}')