num = int(input('Digite um número:'))
U = num // 1 % 10
D = num // 10 % 10
C = num //100 % 10
M = num // 1000 % 10
print('Analizando o número {}'.format(num))
print('Unidade: {}'.format(U))
print('Dezena: {}'.format(D))
print('Centena: {}'.format(C))
print('Milhar: {}'.format(M))
