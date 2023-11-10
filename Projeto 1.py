from time import sleep 

menubolo = { 
    1: ("Pudim", 30.00),
    2: ("Cenoura com Chocolate", 32.00),
    3: ("Brigadeiro", 33.00),
    4: ("Coco com Abacaxi", 34.00),
    5: ("Red Velvet", 35.00),
    6: ("Morango com Chantilly", 36.00),
    7: ("Doce de Leite", 37.00),
    8: ("Mousse de Maracujá", 38.00),
    9: ("Limão Siciliano", 38.00),
    10: ("Cheesecake de Morango", 40.00),
    11: ("Chocolate Belga", 40.00),
    12: ("Tiramisu", 41.00),
    13: ("Baunilha com Framboesa", 39.00),
    14: ("Amêndoas e Caramelo", 42.00),
    15: ("Nozes com Creme", 45.00)
}

def diasemana(): 
    print("\n[1] - Domingo\n[2] - Segunda\n[3] - Terça\n[4] - Quarta\n[5] - Quinta\n[6] - Sexta\n[7] - Sábado") 
    x = int(input("\nQue dia da semana é hoje?: ")) 
    
    if x == 1:
        print("\nInfelizmente nossa loja não abre nos domingos") 
        sleep(2) 
    elif x == 2:
        print("\nNas Segundas, nossa loja atende das 13:00 até as 17:00")
        sleep(2)
    elif x == 3:
        print("\nNas Terças, nossa loja atende das 13:00 até as 17:00")
        sleep(2)
    elif x == 4:
        print("\nNas Quartas, nossa loja atende das 13:00 até as 17:00")
        sleep(2)
    elif x == 5:
        print("\nNas Quintas, nossa loja atende das 13:00 até as 17:00")
        sleep(2)
    elif x == 6:
        print("\nNas Sextas, nossa loja atende das 13:00 até as 17:00")
        sleep(2)
    elif x == 7:
        print("\nNos Sábados, nossa loja atende das 11:00 até as 15:00")
        sleep(2)
    else:
        print("\nOpção inválida") 
        sleep(2)

def seupedido(): 
    preçobolo = [] 
    preçototal = 0 

    while True: 
        print("\nEscolha o sabor do bolo (digite 0 para finalizar seu pedido):") 
        for bolo1, (sabor, preço) in menubolo.items(): 
            print(f"[{bolo1}] - {sabor} - R$ {preço:.2f}") 
        
        escolha = int(input("Digite os sabores desejados: ")) 

        if escolha == 0: 
            break 
        elif escolha in menubolo: 
            sabor, preço = menubolo[escolha] 
            preçobolo.append(sabor) 
            preçototal += preço 
            print(f"\nVocê escolheu: {sabor} - R$ {preço:.2f}") 
        else:
            print("\nOpção inválida")

    if preçobolo:
        print("\nPedido:")
        for bolo in preçobolo:
            print(bolo)
        print(f"Total a pagar: R$ {preçototal:.2f}") 
        print("\nNos informe seu endereço: ")
        input("\nBairro: ")
        input("Rua: ")
        input("Número: ")
        input("Complemento: ")
        print("\n Nossa chave pix para realizar o pagamento é: 'Imagine uma chave pix inserida aqui ok'") 
        sleep(3)
        print("\nAgradecemos por seu pedido, após o pagamento ser efetuado, seu pedido sairá para a entrega. Obrigado pela confiança")
        sleep(3)

def main_menu(): 
    while True: 
        print("\n------------------------------------------")
        print("\nOlá, seja bem-vindo(a) a nossa loja Cakes da Gabriela, o que gostaria?")
        print("\n[1] - Fazer pedido\n[2] - Cardápio e valores\n[3] - Saber mais sobre a empresa\n[4] - Status da loja\n[0] - Sair") 
        x = int(input("\nDigite a opção desejada: "))

        if x == 0:
            break 
        elif x == 1:
            seupedido() 
        elif x == 2:
            print("\nCardápio e valores:")
            for sabor, (nome, preço) in menubolo.items(): 
                print(f"{sabor} - {nome} - R$ {preço:.2f}") 
            sleep(5)
        elif x == 3:
            print("\nNós somos a empresa Cakes da Gabriela, temos mais de 5 anos já no mercado vendendo bolos\nAtualmente atendemos na região de Cinelândia e Botafogo\nNosso compromisso é com sua satisfação, realizando sonhos em cada fatia")
            sleep(3)
        elif x == 4:
            diasemana() 
            print("\nOpção inválida")
            sleep(2)

main_menu() 
