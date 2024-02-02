# 1.) Crie um programa que exiba a seguinte frase:

nome = ("Gustavo")
idade = ("22")
cidade = ("Jandira")
# Apresentação com virgula (a virgula ja deixa o formato da execução organizado).
print("meu nome é" , nome ,"tenho", idade ,"anos e moro em", cidade)
# Apresentação usando mais (deixa o formato)
print("Meu nome é " + nome + "tenho" + idade + "anos e moro em" + cidade)

# 2.)crie um programa que imprima os operadores aritméticos: +, -, *, /, %, **, //
# Soma
print("Operador de soma (+):", 5 + 3)

# Subtração
print("Operador de subtração (-):", 5 - 3)

# Multiplicação
print("Operador de multiplicação (*):", 5 * 3)

# Divisão
resultado = 5/3
print(f"Operador de divisão (/): {resultado:.2f}")

# Módulo (resto da divisão)
print("Operador de módulo (%):", 5 % 3)

# Exponenciação
print("Operador de exponenciação (**):", 5 ** 3)

# Divisão inteira
print("Operador de divisão inteira (//):", 5 // 3)

# 3.) Crie um programa ultilizando os operadores de comparação: ==, !=, >, >=, <, <=.

# Igual
print("Operador igual (==)", 5 == 3)

# Diferente de
print("Operador diferente de (!=)", 5 != 3)

# Maior que 
print("Operador maior que (>)", 5 > 3)

# Maior ou igual que 
print("Operador igual (>=)", 5 >=3)

# menor que
print("Operador igual (<)", 5 < 3)

# Menor ou igual que
print("Operador igual (<=)", 5 <= 3)

# Construa um programa que faça o seguinte calculo um aumento de 15% para um salario de R$: 1000,00

# Salário inicial
salario_inicial = 1000.00

# Percentual de aumento
percentual_aumento = 15

# Calcula o aumento
aumento = salario_inicial * (percentual_aumento / 100)

# Calcula o novo salário após o aumento
novo_salario = salario_inicial + aumento

# Imprime os resultados
print(f"Salário inicial: R$ {salario_inicial:.2f}")
print(f"Percentual de aumento: {percentual_aumento}%")
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")

# 4.) Elabore um programa que exiba o lucro de uma empresa:
# sendo a formula lucro = faturamento - 

# Solicita ao usuário para inserir o faturamento e o custo
faturamento = float(input("Digite o faturamento da empresa: "))
custo = float(input("Digite o custo total da empresa: "))

# Calcula o lucro
lucro = faturamento - custo

# Exibe o resultado
print(f"O lucro da empresa é: R${lucro:.3f}")

# 5.) Crie um programa que leia um nome digitado pelo teclado e imprima "Olá! + <seu nome>"

nome = (input("Digite um nome: "))
idade = (input("Digite sua idade: "))
print(f"Olá! {nome}, Você tem {idade}")

# 6.)A partir da digitação da base e altura de um triangulo o programa devera calcular sua area e exibi-la no monitor.

# Solicita a entrada do usuário para a base e altura do triângulo
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

# Calcula a área do triângulo usando a fórmula: área = (base * altura) / 2
area = (base * altura) / 2

# Exibe a área calculada
print(f"A área do triângulo com base {base} e altura {altura} é: {area}")

# 7.) Escreva um programa que leia um valor em metros e o exiba convertido em milimetros.

# Solicita ao usuário que digite um valor em metros.
metros = float(input("Digite o valor em metros: "))

# Converte metros para milímetros (1 metro = 1000 milímetros).
milimetros = metros * 1000

# Exibe o resultado da conversão.
print(f"{metros} metros equivalem a {milimetros} milímetros.")

# 1.) Crie um programa que exiba a seguinte frase.

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")

print(f"Meu nome é {nome}, tenho {idade} anos e moro em {cidade}")

