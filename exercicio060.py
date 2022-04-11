cont = 1
n = int(input('Digite o número que você deseja saber o fatorial: '))
while n >= 1:
    cont *= n
    n = n - 1
print(cont)