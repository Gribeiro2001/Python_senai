#criação do Outer for loop
for numero1 in range(5):
    print(numero1)
#criação do Inner for loop
for numero2 in range(5):
    print(numero1, numero2) 

#criação do Outer for loop
for numero1 in range(1,6):
    print("Produto", str(numero1))
#criação do Inner for loop
for numero2 in range(11):
    print(numero1, numero2)

palavra = "fantastico"
#declaração for
for spaco in palavra:
    print(spaco, end =" ")

palavra = "fantastico"
#declaração for
for spaco in palavra:
    print(f" {spaco}", end =" ")

#modificando de fantastico para f a n t a s t i c o
#palavra = str(input("Digite uma palavra: "))
#for spaco in palavra:
 #   print(f" {spaco}", end =" ")

# criando um retangulo 6x6
linhas = 6
colunas = 6
simbolo = "%"
for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end =" ")
    print()