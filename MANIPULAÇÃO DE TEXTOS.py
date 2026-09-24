# Escreva um programa que conta o número de vogais e consoantes em uma string
frase1 = 'Contando o número de vogais e consoantes.'
numero_de_palavras =    len(frase1.split())
print(f'A frase tem {numero_de_palavras} palavras.')


# Escreva um programa que verifica se uma string é um palíndromo.
palavra = 'arara'
if palavra == palavra[::-1]:
    print(f'{palavra} é um palíndromo')
else:
    print(f'{palavra} não é um palíndromo')

# Escreva um programa que conta o número de palavras em uma frase.
frase = "Contabilizando o número de palavras dessa frase."
palavras = frase.split()
quantidade = len(palavras)
print(f'A frase contém {quantidade} palavras.')

# Escreva um programa que capitalize a primeira letra de cada palavra em uma frase.
titulo = "aprendendo python no senac"
titulo_formatado = titulo.title()
print(titulo_formatado)
