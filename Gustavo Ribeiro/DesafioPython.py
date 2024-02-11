# 1.)Para este desafio, quero que você crie um código que imprima a frase “Bom dia <seu nome>  

# Solicita ao usuário que insira o nome
seu_nome = input("Digite seu nome: ")
print(f"Bom dia {seu_nome}!")

# 2.)
nome = "Gustavo"
idade = 23
print(f"Oi meu nome é {nome} e tenho {idade} anos!")
 
# 3.)
num1 = 10
num2 = 3.5
resultado_divisao = num1 / num2
print(f"O resultado da divisão de {num1} por {num2} é: {resultado_divisao:.2f}")

# 4.)
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
endereco = input("Digite seu endereço: ")
print(f"Bem-vindo, {nome}! Você tem {idade} anos e mora no endereço {endereco}.")

# 5.)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
exponenciacao = num1 ** num2
# Imprime os resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao:.2f}")
print(f"Exponenciação: {exponenciacao}")

#6.)
for numero in range(1, 11):
    print(numero)

#7.)
def calcular_preco_passagem(km):
    if km > 200:
        preco = km * 0.45
    else:
        preco = km * 0.50
    return preco

quilometragem = float(input("Informe a quilometragem da viagem: "))
preco_total = calcular_preco_passagem(quilometragem)
print(f"O preço da passagem é: R${preco_total:.2f}")






