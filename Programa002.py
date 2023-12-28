import random
n1 = str(input('Digite o nome do seu primeiro amigo:'))
n2 = str(input('Digite o nome do seu segundo amigo:'))
n3 = str(input('Digite o nome do seu terceiro amigo:'))
n4 = str(input('Digite o nome do seu quarto amigo:'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apressentação será:')
print(lista)
