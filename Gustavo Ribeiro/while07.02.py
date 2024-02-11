# Pergunta ao usuário se deseja iniciar o programa
resp = input("Deseja iniciar o programa? s/n ")
# Enquanto a resposta não for 's' (sim) e nem 'n' (não)...
while resp != "s" and resp != "n":
    # Pede uma nova resposta ao usuário, pois a anterior foi inválida
    resp = input("Resposta inválida!!! Deseja continuar? s/n")
# Quando a resposta for válida, imprime uma mensagem informando que o programa continuará
print("Resposta ok. Vamos continuar o programa")
# Imprime uma mensagem indicando o fim do programa
print("Fim do programa")
# Pede ao usuário para digitar um número para ser somado, com a opção de parar digitando 999
n = int(input("Digite um número para ser somado: [999 - para parar]"))
soma = 0
# Enquanto o número digitado não for 999...
while n != 999:
    # Adiciona o número à variável soma
    soma += n
    # Pede ao usuário para digitar outro número para ser somado, ou 999 para parar
    n = int(input("Digite outro número para ser somado com os anteriores: 999 - para sair "))
# Ao final do loop, imprime a soma dos números digitados
print("Soma = {}".format(soma))
# Pede ao usuário para digitar uma senha
senha = input("Digite sua senha: ")
senha_correta = "123"
# Enquanto a senha digitada for diferente da senha correta...
while senha != senha_correta:
    # Informa ao usuário que a senha está incorreta e solicita uma nova tentativa
    print("Senha incorreta! Tente novamente")
    senha = input("Digite sua senha: ")
# Quando a senha correta for digitada, imprime uma mensagem indicando acesso permitido
print("Acesso permitido!")
# Reinicializa a variável senha_digitada
senha_digitada = ''
# Enquanto a senha digitada não for igual à senha correta...
while senha_correta != senha_digitada:
    # Pede ao usuário para digitar a senha
    senha_digitada = input('Digite sua senha: ')
    # Se a senha digitada for diferente da senha correta, informa ao usuário que a senha está incorreta
    if senha_correta != senha_digitada:
        print('Senha incorreta, tente novamente!')
# Quando a senha correta for digitada, imprime uma mensagem de boas-vindas ao sistema
print('Bem-vindo ao sistema!')

# Solicita ao usuário a quantidade de termos da sequência de Fibonacci que deseja gerar
qtde = int(input("Quantos termos do fibonacci você deseja? "))
# Define os dois primeiros termos da sequência de Fibonacci
anterior = 0
atual = 1
# Inicializa o contador para controlar o número de termos já gerados
contador = 1
# Enquanto o contador for menor ou igual à quantidade desejada de termos...
while contador <= qtde:
    # Imprime o termo atual da sequência de Fibonacci, seguido de um hífen, sem quebra de linha
    print("{} -".format(atual), end=" ")
    # Calcula o próximo termo da sequência de Fibonacci somando os dois últimos termos
    proximo = anterior + atual 
    # Atualiza os termos anteriores para os próximos cálculos
    anterior = atual
    atual = proximo   
    # Incrementa o contador para acompanhar quantos termos já foram gerados
    contador += 1
# Quando o loop terminar (ou seja, quando a quantidade desejada de termos for alcançada),
# imprime uma mensagem indicando o fim do programa de Fibonacci
print("fim do programa de fibonacci")
print(contador)

# Inicializa a variável 'soma' para armazenar a soma dos números digitados
soma = 0
# Inicializa a variável 'qtdenumeros' para contar a quantidade de números digitados (começando com 1)
qtdenumeros = 1
# Inicializa a variável 'resp' como 's', permitindo que o loop seja executado pelo menos uma vez
resp = "s"
# Enquanto a resposta for 's' (sim), o loop continuará executando
while resp == "s":
    # Solicita ao usuário que digite um número
    n = int(input("Digite um número: "))
    # Se for o primeiro número digitado, inicializa as variáveis 'maior' e 'menor' com este número
    if qtdenumeros == 1:
        maior = n
        menor = n 
    # Se o número digitado for maior que o atual 'maior', atualiza o valor de 'maior'
    if n > maior:
        maior = n
    # Se o número digitado for menor que o atual 'menor', atualiza o valor de 'menor'
    if n < menor:
        menor = n
    # Adiciona o número à variável 'soma'
    soma += n
    # Pergunta ao usuário se deseja continuar digitando números
    resp = input("Deseja continuar digitando? (s/n) ")
    # Enquanto a resposta não for 's' ou 'n', solicita que o usuário informe corretamente
    while resp != "s" and resp != "n":
        resp = input("Informe corretamente se deseja continuar digitando: (s/n) ")
    # Se a resposta for 's', incrementa a quantidade de números digitados
    if resp == "s":
        qtdenumeros += 1
# Após o loop terminar (quando a resposta não for mais 's'), imprime os resultados
print("Quantidade de números somados: {}".format(qtdenumeros))
print(f"Soma = {soma}")
print(f"Menor número entre os digitados foi {menor}")
print(f"Maior número entre os digitados foi {maior}")

# Inicializa as variáveis para armazenar a soma dos números e contar quantos números foram digitados
soma = cont = 0
# Loop principal que continuará indefinidamente até ser interrompido explicitamente
while True:
    # Solicita ao usuário que digite um número
    n = int(input("Digite um número: "))
    # Se o número digitado for igual a 999, o loop será interrompido
    if n == 999:
         break  # Esta linha interrompe o loop quando n for igual a 999  
    # Incrementa o contador de números digitados
    cont += 1
    # Adiciona o número à soma total
    soma += n
# Após o término do loop, imprime a quantidade de números digitados e a soma total
print(f"Você somou {cont} números")
print(f"A soma de todos foi {soma}")





