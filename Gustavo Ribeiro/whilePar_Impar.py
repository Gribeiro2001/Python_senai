# Importa o módulo random para gerar números aleatórios
import random
# Inicializa as variáveis para contar os pontos do usuário e do computador
ptsusuario = ptscomputador = 0
# Loop principal que continuará indefinidamente até ser interrompido explicitamente
while True:
    # Solicita ao usuário que digite um número entre 0 e 10
    n = int(input("Qual número entre 0 e 10? "))
    # Pergunta ao usuário se escolhe par ou ímpar
    parouimpar = input("Par ou ímpar? Responda: p/i ")
    # Enquanto a resposta do usuário não for 'p' (par) nem 'i' (ímpar), pede novamente
    while parouimpar != "p" and parouimpar != "i":
        parouimpar = input("Resposta inválida! Responda: p/i ")
    # Gera um número aleatório para representar a escolha do computador
    computador = random.randint(0, 10)
    # Calcula a soma dos números escolhidos pelo usuário e pelo computador
    soma = n + computador
    # Verifica se a soma é par e se o usuário escolheu par, então atribui ponto ao usuário
    if soma % 2 == 0 and parouimpar == "p":
        ptsusuario += 1
    # Verifica se a soma é ímpar e se o usuário escolheu ímpar, então atribui ponto ao computador
    elif soma % 2 == 1 and parouimpar == "i":
        ptscomputador += 1
    # Se nenhuma das condições acima for verdadeira, o computador ganha um ponto
    else:
        ptscomputador += ptscomputador
        break  # Sai do loop principal
# Após o término do loop, exibe o número de partidas vencidas pelo usuário
print(f"Você venceu {ptsusuario} partidas")
print(f"computador venceu {ptscomputador} partidas")
