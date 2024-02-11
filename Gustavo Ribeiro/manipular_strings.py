# Atribuindo a string "Apostila de Python" à variável palavra
palavra = "Apostila de Python"
# len() retorna o comprimento da string, ou seja, o número de caracteres.
print(len(palavra))
# capitalize() retorna a string com a primeira letra em maiúscula e as demais em minúscula.
print(palavra.capitalize())
# count() retorna o número de ocorrências de uma determinada substring dentro da string.
print(palavra.count("o"))
# startswith() verifica se a string começa com a substring especificada e retorna True ou False.
print(palavra.startswith("Ap"))
# endswith() verifica se a string termina com a substring especificada e retorna True ou False.
print(palavra.endswith("Py"))
# isalnum() verifica se todos os caracteres da string são alfanuméricos (letras ou números) e retorna True ou False.
print(palavra.isalnum())
