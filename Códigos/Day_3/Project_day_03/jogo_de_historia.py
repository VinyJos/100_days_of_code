'''Project Day 3
Montando um jogo com história'''

print('Esta é a história do tesouro perdido.')
print('Em 1892, um pirata enterrou ouro na Ilha Adak no valor de mais de US$ 300.000.000.Ele morreu antes que pudesse retornar. Agora você tem a chance de achar e levar as moedas de ouro para casa. Mas existem muitas armadilhas então faça a escolha certa e bora pro jogo !!!')

começar = input('Começar : Sim ou não ?\n').lower()

if começar == 'sim' or começar == 's':
    print('Você está em um barco indo em direção a Ilha, qual lugar da ilha deseja desembarcar ? ')
    print('1- Centro  militar abandonado')
    print('2- Sul da ilha, entrada escondida')
    print('3 - Lago principal, no meio da Ilha') 
    desembarque = int(input('Escolha um número acima!\n'))
    #encadeamento desembarque centro militar abandonado
    #-------------------------------------------------------------------------------------------------------------------
    if desembarque == 1:
        print('Você está no centro  militar abandonado agora.\nVocê está em um local cheio de ferramentas e equipamentos para utilizar ao seu favor, qual ferramenta você vai escolher ?')

        print('1- Pá de bico.')
        print('2-Sensor leitor de metais.')
        print('3-Trator')
        ferramenta = int(input('Escolha um número acima!\n'))

        if ferramenta == 1:
            print('Após um dia inteiro cavando, você não achou nada !\nQuem sabe na próxima você tem mais sorte!\nFim de jogo para você !')

        elif ferramenta == 2:
            print('Após algumas horas fazendo a leitura com seu equipamento, você conseguiu achar um objeto que está em baixo da terra! Parabéns \nMas você precisa desenterrar. Tens direito a mais uma ferramenta !')

            print('1- Pá de bico\n 2- Trator')

            ferramenta2 = int(input('Escolha um número acima!\n'))
            if ferramenta2 == 1:
                print('**Pá de bico**\n\nBOOOOMMMM \n…morreu\n \nnão era um tesouro mas uma bomba deixada pelos militares.\nfim de jogo')
            elif ferramenta2 == 2:
                print('BOOOOMMMM… \n\nNão era um tesouro mas uma bomba deixada pelos militares.\n Você está bem mas seu trator não! \n\nTem a chance de procurar em outro lugar, ou pode Desistir agora, o que você escolhe ?')

                print('1- Procurar em outro lugar')
                print('2- Ir embora sem nada')

                decisao = int(input('Escolha um número acima!\n'))
            
            if decisao == 1:
                print('continua...')
            elif decisao == 2:
                print('Fim de jogo')

            #por enquanto esse é o fim do encadeamento do desembarque centro militar abandonado
            #--------------------------------------------------------------------------------------------------------------
    elif desembarque == 2:
        print('Você está no Sul da ilha, entrada escondida agora')
    elif desembarque == 3:
        print('Você está no Lago principal, no meio da Ilha agora')



else:
    print('Fim!')