# Criando um dicionário 'd' que mapeia produtos a seus preços.
d = {
    "arroz": 17.30,
    "feijao": 12.50,
    "carne": 23.90,
    "alface": 3.40
}
print(d) 

# Imprimindo o preço da carne, acessando o valor correspondente à chave "carne" no dicionário.
print(d["carne"])

# Atualizando o valor associado à chave "carne" e adicionando a chave "tomate" com seu respectivo valor.
d = {"arroz": 17.30, "feijao": 12.50, "carne": 23.90, "alface": 3.40}
d["carne"] = 25.0  # Atualizando o valor da chave "carne" para 25.0
d["tomate"] = 8.80  # Adicionando a chave "tomate" com o valor 8.80
print(d)  

# Operações com dicionarios

dx = {
    2:"carro",
    3:[4,5,6],
    7:("a","b"),
    4: 173.8
}
print(dx[7])
print(dx[3])
print(dx[2])

# Criando um dicionário
dicionario = {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}
# Acessando um valor através de uma chave
valor = dicionario["chave2"]
print("Valor associado à chave2:", valor)
# Adicionando um novo elemento ao dicionário
dicionario["chave4"] = "valor4"
print("Dicionário após adicionar um novo elemento:", dicionario)
# Removendo um elemento do dicionário
del dicionario["chave3"]
print("Dicionário após remover o elemento associado à chave3:", dicionario)
# Iterando sobre os pares chave-valor do dicionário
print("Pares chave-valor do dicionário:")
for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")
