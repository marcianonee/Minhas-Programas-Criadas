frase = str(input('Escreve uma frase:'))
print(' A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
