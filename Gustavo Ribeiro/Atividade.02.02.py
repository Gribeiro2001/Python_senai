# criar um codigo que exiba que eu coloque a idade do meu carro

#ano_fabricacao =float (input("Informe o ano fabricacao do seu carro: "))
#resultado = 2024 - ano_fabricacao

#if resultado > 3:
 #   print("Seu carro é velho")
#if resultado <= 3:
  #  print("Seu carro é novo")

#Abaixo de 200 cobra 0.20 entre 200 e 400 cobra 0.18 acima de 400 o preço é 0.15
# Metodo de estrutura aninhada.
minutos = int(input("Quantos minutos você utilizou este mês: "))

if minutos < 200:
    preco = 0.20
elif minutos > 400:
    preco = 0.15
else:
    preco = 0.18

total_pagar = minutos * preco
print(f"Você vai pagar este mês: R${total_pagar:6.2f}")

# crie um programa simples para saber se uma pessoa pode fazer um financiamento:
# requisitos : uma renda acima de R$ 5.000.00 seu nome deve esta limpo

renda = 5000
status = "limpo"

if renda > 5000 and status == "limpo":
    print("Você pode financiar. ")
else:
    print("Você não pode financiar. ")

renda = 5000
status = "limpo"

if renda > 5000 or status == "limpo":
    print("Você pode financiar. ")
else:
    print("Você não pode financiar. ")

valor = float(input("Insire um valor: "))

if valor >= 20 and valor <40:
    print("O produto pode ser inserido")
else:
    print("O produto não pode ser inserido")

# Podemos melhorar o codigo de uma forma mais matematica
valor = 0 
#melhorar sintaxe de forma matematica 
if 20<= valor <40:

#if valor >= 20 and valor <40:
    print("produto foi aceito")
else:
    print("Produto não aceito")

# Obtenha as quatro notas do usuário
nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))

# Calcule a média aritmética
media = (nota1 + nota2 + nota3 + nota4) / 4

# Verifique a condição de aprovação, reprovação ou exame
if media >= 6:
    print(f"Sua média final é {media:.2f}. Você está APROVADO!")
elif media < 3:
    print(f"Sua média final é {media:.2f}. Você está REPROVADO.")
else:
    print(f"Sua média final é {media:.2f}. Você está em EXAME.")
