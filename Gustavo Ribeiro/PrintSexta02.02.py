# Função type é utilizada para obter o tipo de um objeto. 
b = "olá"
print(b,type(b))

# atribuições
x=10
x-5
print(x)

# Aqui, MinhaClasse é uma classe recém-criada usando type(), e objeto_da_classe é uma instância dessa classe. 
MinhaClasse = type('MinhaClasse', (), {})
objeto_da_classe = MinhaClasse()

a= int (input("Primeiro valor: "))
b= int (input("Segundo valor: "))

# Ele é usado para executar um bloco de código condicionalmente
if a > b:
    print("O primeiro numero é o maior")
if b > a:
    print("O segundo numero é maior")

salario = float(input("Digite o salario para calculo do imposto: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto +((base - 3000)* 0.35)
    base = 3000
if base >= 1000:
    imposto = imposto + ((base - 1000)*0.20)
print("salario: R$%6.2f Imposto a pagar: R$%6.2f" % (salario,imposto))

# ELSE condição senão

a = int(input("Digite a idasde do seu carro: "))
if a <=3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")

x = 2 < 3 and 2 == 4
y = 2 < 3 or 2 == 4
z = not 1 == 1
print(x, type(x))
print(y, type(y))
print(z, type(y))

# Operadores de comparação 

