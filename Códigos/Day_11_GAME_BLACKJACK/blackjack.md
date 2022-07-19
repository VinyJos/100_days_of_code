# ############## Projeto Blackjack #####################

#Dificuldade Normal 😎: Use todas as Dicas abaixo para concluir o projeto.
#Dificuldade Difícil 🤔: Use apenas as Dicas 1, 2, 3 para concluir o projeto.
#Dificuldade Extra Difícil 😭: Use apenas as Dicas 1 e 2 para concluir o projeto.
#Especialista em Dificuldades 🤯: Use apenas a Dica 1 para concluir o projeto.

# ############## Nossas Regras da Casa do Blackjack ######################

## O baralho é ilimitado em tamanho.
## Não há curingas.
## O Valete/Rainha/Rei contam como 10.
## O Ás pode contar como 11 ou 1.
## Use a seguinte lista como o baralho de cartas:
## cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## As cartas da lista têm a mesma probabilidade de serem sorteadas.
## As cartas não são removidas do baralho à medida que são compradas.
## O computador é o revendedor.

# #################### Dicas ######################

#Dica 1: Acesse este site e experimente o jogo de Blackjack:
# https://games.washingtonpost.com/games/blackjack/
#Então experimente o projeto Blackjack completo aqui:
# http://blackjack-final.appbrewery.repl.run

#Dica 2: Leia este detalhamento dos requisitos do programa:
# http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Em seguida, tente criar seu próprio fluxograma para o programa.

#Dica 3: Baixe e leia este fluxograma que criei:
# https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Dica 4: Crie uma função deal_card() que use a Lista abaixo para *retornar* um cartão aleatório.
#11 é o Ás.
#cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Dica 5: Dê ao usuário e ao computador 2 cartas cada usando deal_card() e append().
#user_cards = []
#computer_cards = []

#Dica 6: Crie uma função chamada calculate_score() que receba uma Lista de cartões como entrada
#e retorna a pontuação.
#Procure a função sum() para ajudá-lo a fazer isso.

#Dica 7: Dentro de calculate_score() verifique se há um blackjack (uma mão com apenas 2 cartas: ás + 10) e retorne 0 em vez da pontuação real. 0 representará um blackjack em nosso jogo.

#Dica 8: Dentro de calculate_score() verifique se há um 11 (ás). Se a pontuação já for superior a 21, remova o 11 e substitua-o por 1. Pode ser necessário procurar append() e remove().

#Dica 9: Chame calculate_score(). Se o computador ou o usuário tiver um blackjack (0) ou se a pontuação do usuário for superior a 21, o jogo termina.

#Dica 10: Caso o jogo não tenha terminado, pergunte ao usuário se ele deseja comprar outra carta. Se sim, use a função deal_card() para adicionar outro cartão à lista user_cards. Se não, então o jogo terminou.

#Dica 11: A pontuação deverá ser verificada novamente a cada nova carta retirada e as verificações da Dica 9 precisam ser repetidas até o fim do jogo.

#Dica 12: Assim que o usuário terminar, é hora de deixar o computador jogar. O computador deve continuar tirando cartas enquanto tiver uma pontuação menor que 17.

#Dica 13: Crie uma função chamada compare() e passe o user_score e computer_score. Se o computador e o usuário tiverem a mesma pontuação, é um empate. Se o computador tiver um blackjack (0), o usuário perde. Se o usuário tiver um blackjack (0), então o usuário ganha. Se o user_score for superior a 21, o usuário perde. Se o computer_score for superior a 21, o computador perde. Se nenhuma das opções acima, então o jogador com a maior pontuação ganha.

#Dica 14: Pergunte ao usuário se ele deseja reiniciar o jogo. Se eles responderem sim, limpe o console e inicie um novo jogo de blackjack e mostre o logotipo do art.py.