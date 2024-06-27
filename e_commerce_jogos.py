#função visualizar carrinho??????

#dados do cartão do cliente
#nome - ***
#validade do cartao - ***
#cvv - ***
saldo_disponivel = 3300.0

#banco_dados() :
jogos = ["Red Dead Redemption 2", "GTA V", "Fifa 24", "Minecraft", "Elden ring"]
preco = [299.9, 82.0, 359.0, 74.9, 229.9]
carrinho = []
preco_total = 0

def menu_incial() :
  global preco_total
  print("Bem-vindo a loja de jogos")
  fechar_menu = False

  while(fechar_menu == False) :
    try :
      cod_funcao = int(input("Digite um código para a função desejada:\n 1- Exibir jogos disponívies\n 2- Carrinho de compras\n 3- Fechar menu "))
      if(cod_funcao == 1) :
        lista_jogos()
        jogo = input("Entre com o nome do jogo para ver mais informações: ")
        for i in range(len(jogos)) :
          if(jogo == jogos[i]) :
            jogo_result = jogos[i] + ": Preço: " + str(preco[i]) + " reais"
            print(jogo_result)
            print("Dejesa adicionar o jogo no carrinho? (S/N)")
            resposta = input()
            if(resposta == "S" or resposta == "s") :
              carrinho.append(jogo)
              preco_total += preco[i]
              print("Jogo adicionado ao carrinho!")
            break
        else :
          print("Jogo não encontrado")
      elif(cod_funcao == 2) :
          carrinho_compras()
      elif(cod_funcao == 3) :
        fechar_menu = True
        print("Menu fechado!")
      else :
        print("Código inválido!")
    except :
      print("Erro! Caractere inválido: o código precisar ser um número. ")


def lista_jogos() :
  print("Jogos disponíveis: " + str(jogos))

def carrinho_compras() :
  global preco_total
  global saldo_disponivel
  global carrinho
  fechar_carrinho = False

  while(fechar_carrinho == False) :
    try :
      cod_funcao = int(input("Digite um código para a função desejada:\n 1- Remover jogo\n 2- Finalizar pedido\n 3- Fechar carrinho "))
      if(cod_funcao == 1) :
        remover_jogo = input("Digite um jogo para remover do carrinho: ")
        for i in carrinho.copy() :
          if(i == remover_jogo) :
            carrinho.remove(i)
            print("Jogo removido do carrinho!")
      elif(cod_funcao == 2) :
        print(carrinho)
        print("Preço total: " + str(preco_total))
        cod_finalizar = input("Dejesa realizar a compra? (S/N)")
        if(cod_finalizar == "S" or cod_finalizar == "s") :
          if(preco_total <= saldo_disponivel) :
            print("Compra finalizada!\nObrigado Volte sempre! ")
            carrinho = []
            preco_total = 0
            fechar_carrinho = True
          else :
            print("Saldo insuficiente!")
        break
      elif(cod_funcao == 3) :
        fechar_carrinho = True
        print("Carrinho fechado!")
      else :
        print("Código inválido!")
    except :
      print("Erro! Caractere inválido: o código precisar ser um número. ")
