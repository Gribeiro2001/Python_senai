palavra = "Apostila Python"

# lower: Converte a string para minúsculas
print(palavra.lower())

# upper: Converte a string para maiúsculas
print(palavra.upper())

# swapcase: Inverte o caso de cada caractere da string, ou seja, converte minúsculas em maiúsculas e vice-versa
print(palavra.swapcase())

# title: Converte a primeira letra de cada palavra para maiúscula e as demais letras para minúscula
print(palavra.title())

# split: Divide a string em uma lista de substrings com base nos espaços em branco (por padrão) e retorna essa lista
print(palavra.split())

# Fatiamento de strings

s = str(input("Digite uma palavra: "))
print(s[1:4])

print(s[2:])

print(s[:4])