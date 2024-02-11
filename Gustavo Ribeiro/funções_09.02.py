# Definindo uma função simples que imprime "Olá Mundo" quando chamada
def hello():
    print("Olá Mundo")
# Chamando a função hello para executar o código dentro dela
hello()

# Exemplo de função que compara dois valores e imprime o maior entre eles
def maior(x, y):
    # Se x for maior que y, imprime x
    if x > y:
        print(x)
    else:
        # Caso contrário, imprime y
        print(y)
# Chamando a função maior com os argumentos 4 e 7
maior(4, 7)

# Exemplo de escopo de variáveis
def soma(x, y):
    # Definindo uma variável local 'total' que armazena a soma de x e y
    total = x + y
    # Imprimindo o total da soma dentro do escopo da função
    print("Total soma = ", total)
# Programa principal
# Definindo uma variável global 'total' com o valor 10
total = 10
# Chamando a função soma com os argumentos 3 e 5
soma(3, 5)
# Imprimindo o valor da variável global 'total'
print("Total principal = ", total)

def soma(x, y):
    # Calcula a soma dos dois números recebidos como parâmetros
    total = x + y
    # Retorna o resultado da soma
    return total
# Programa principal
# Chama a função soma com os números 3 e 5 como argumentos e armazena o resultado na variável 's'
s = soma(3, 5)
# Imprime o resultado da soma
print("soma = ", s)


