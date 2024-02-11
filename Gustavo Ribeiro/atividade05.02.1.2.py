# Simulando se a compra foi bem-sucedida (True) ou falha na compra (False)
compra_bem_sucedida = True
# Definindo o valor da compra
dados_compra = "Compra no valor R$ 12.50 e entrega confirmada."
# Melhorando com loop for para tentativas
for tentativa in range(3):
    # Condição utilizando if-else para determinar a mensagem a ser exibida
    if compra_bem_sucedida:
        print(dados_compra)
        print("Detalhes enviados para o seu email.")
        break
else:
    print("Por favor, entre em contato com o suporte.")
