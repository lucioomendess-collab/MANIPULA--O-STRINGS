# Escreva um programa que conta o número de vogais e consoantes em uma string
texto = input('Digite um texto: ').lower()
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"

total_vogais = 0
total_consoantes = 0

for letra in texto:
  if letra in vogais:
    total_vogais += 1
  elif letra in consoantes: 
    total_consoantes += 1

print(f"Vogais: {total_vogais}")
print(f"Consoantes: {total_consoantes}")

     
# Escreva um programa que verifica se uma string é um palíndromo.
palavra = input('Digite uma palavra: '.lower())
if palavra == palavra[::-1]:
    print(f'{palavra} é um palíndromo')
else:
    print(f'{palavra} não é um palíndromo')

# Escreva um programa que conta o número de palavras em uma frase.
frase = "Contabilizando o número de palavras dessa frase."
palavras = frase.split()
quantidade = len(palavras)
print(f'A frase contém {quantidade} palavras.')

# Escreva um programa que inverte a ordem das palavras em uma frase.

# Escreva um programa que capitalize a primeira letra de cada palavra em uma frase.
titulo = "aprendendo python no senac"
titulo_formatado = titulo.title()
print(titulo_formatado)



