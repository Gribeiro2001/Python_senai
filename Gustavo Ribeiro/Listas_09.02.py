# Criando uma lista com diferentes tipos de dados
L = [3, "abacate", 9.7, [5, 6, 3], "python", (3, "j")]
# Imprimindo o terceiro elemento da lista L (índice 2)
print(L[2])
# Imprimindo o quarto elemento da lista L (índice 3), que é outra lista
print(L[3])
# Imprimindo o segundo elemento da lista dentro do quarto elemento de L
print(L[3][1])
# Reatribuindo o quarto elemento da lista L com a entrada do usuário convertida para string
L[3][1] = str(input("Digite uma palavra ou um número: "))
# Imprimindo a lista L atualizada
print(L)

# Criando uma lista com elementos numéricos
L = [1, 2, 3, 4]
# len: Retorna o número de elementos na lista
print(len(L))
# min: Retorna o menor elemento da lista
print(min(L))
# max: Retorna o maior elemento da lista
print(max(L))
# sum: Retorna a soma de todos os elementos da lista
print(sum(L))
# in: Verifica se um elemento está presente na lista (retorna True se estiver, False caso contrário)
print(3 in L)

# Operações com listas

# Concatenação (+)
a = [0,1,2]
b = [3,4,5]
c = a+b
print(c)[0,1,2,3,4,5]

# Repetição (*)
l = [1,2]
r = l*4
print(r)

# Criando uma lista 'l1' contendo os números de 0 a 4 usando a função range(), que gera uma sequência de números.
# A função list() é utilizada para converter a sequência gerada por range() em uma lista.
l1 = list(range(5))
print(l1)  # Saída: [0, 1, 2, 3, 4]
# Criando uma lista 'l2' contendo os números de 3 a 7 usando a função range().
l2 = list(range(3, 8))
print(l2)  # Saída: [3, 4, 5, 6, 7]
# Criando uma lista 'l3' contendo os números de 2 a 10, com um passo de 3 unidades entre eles.
l3 = list(range(2, 11, 3))
print(l3)  # Saída: [2, 5, 8]


