'''
Jogo blackjack
Q= 10
J= 10
K= 10
A= 1 ou 11
se passar de 21 pontos perde.
começa pedindo carta até completar 21pontos, se quiser pode parar com menos pontos, depois vem a banca e faz o mesmo processo se ultrapassar 21 pontos também perde
ganha quem tiver mais pontos e até 21 pontos
'''
import random
start = 'y'

while start == 'y':
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # GERANDO 2 CARTAS ALEATÓRIAS PRA CADA
    user_cards = []
    computer_cards = []
    points_user_card = 0
    points_computer_card = 0
    for card in range(0, 2):
        user_cards.append(random.choice(cards))
        points_user_card += user_cards[card]
        computer_cards.append(random.choice(cards))
        points_computer_card += computer_cards[card]

    # PRINT DO RESULTADO
    print(f"Your cards: {user_cards}, current score: {points_user_card}")
    print(f"Computer's first card: {computer_cards[0]}")

    # VER QUEM GANHOU
    if points_computer_card == 21 and points_user_card == 21:
        print(f"computer's final hand: {computer_cards}, final score: {points_computer_card}")
        print(f'Computer Blackjack ! Gain with {points_computer_card} points.')
    elif points_user_card == 21:
        print(f"computer's final hand: {computer_cards}, final score: {points_computer_card}")
        print(f'User Blackjack ! Gain with {points_user_card} points.')
    elif points_computer_card == 21:
        print(f"computer's final hand: {computer_cards}, final score: {points_computer_card}")
        print(f'Computer Blackjack ! Gain with {points_computer_card} points.')
    else:
        # PERGUNTA SE O USUÁRIO QUER MAIS CARTA OU PASSAR A VEZ
        most_card = input("\nType 'y' to get another card, type 'n' to pass: ")
        while most_card == 'y':
            pointss = 0
            card1 = (random.choice(cards))
            user_cards.append(card1)
            points_user_card += card1

            if points_user_card > 21:
                for point__ in user_cards:
                    if point__ == 11:
                        pointss = 1
                if pointss != 0:
                    points_user_card -= 10

            print(f"Your cards: {user_cards}, current score {points_user_card}")
            print(f"Computer's first card: {computer_cards[0]}")

            if points_user_card > 21:
                most_card = False
            else:
                most_card = input("\nType 'y' to get another card, type 'n' to pass: ")

            
            
            
        # TESTANDO OS PONTOS DO COMPUTADOR
        if most_card == False:
            print(f"\nYour final hand: {user_cards}, final score: {points_user_card}")
            print(f"computer's final hand: {computer_cards}, final score: {points_computer_card}")
            print("\nYou went over.You lose !")
        else: 
            while points_computer_card <= 17 or points_computer_card < points_user_card:
                pointss2 = 0 
                card2 =  (random.choice(cards))
                computer_cards.append(card2)
                points_computer_card += card2

                if points_computer_card > 21:
                    for point_ in computer_cards:
                        if point_ == 11:
                            pointss2 = 1
                            
                    if pointss2 != 0:
                        points_computer_card -= 10
                        
            
            
            
            print(f"Your final hand: {user_cards}, final score: {points_user_card}")
            print(f"computer's final hand: {computer_cards}, final score: {points_computer_card}")
                

            # TESTANDO QUEM GANHOU
            if points_user_card == points_computer_card :
                print("\nGame tied")
            
            elif points_user_card > points_computer_card:
                if points_user_card <= 21:
                    print("\nYou Gain !!!")
                else:
                    print("\nYou went over.You lose !")
            else:
                if points_computer_card <= 21:
                    print("\nYou went over.You lose !")
                else:
                    print("\nYou Gain !!!")

    start = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
        
