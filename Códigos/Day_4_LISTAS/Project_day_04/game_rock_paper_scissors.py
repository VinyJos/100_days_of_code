''' Projeto consiste em fazer um jogo de pedra, papel e tesoura contra o computador. '''

import random

print('Bem vindo ao jogo! Pedra, papel e tesoura!')
usuario = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura."))

pedra = 0
papel = 1
tesoura = 2
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer = random.randint(0, 3)

if usuario == pedra:
    print(rock)
    print('Você escolheu Pedra')
    print()
    if computer == pedra:
        print(rock)
        print('Empate! \nComputador escolheu pedra também.')
    elif computer == papel:
        print(paper)
        print('Computador escolheu papel ! \nComputador ganhou! \nPapel enrola pedra.')
    elif computer == tesoura:
        print(scissors)
        print('Computador escolheu tesoura. \nVocê ganhou! \nPedra quebra a tesoura!')

elif usuario == papel:
    print(paper)
    print('Você escolheu papel')
    if computer == papel:
        print(paper)
        print('Empate! \nComputador escolheu papel também.')
    elif computer == pedra:
        print(rock)
        print('Computador escolheu pedra! \nVocê ganhou! \n Papel embrulha a pedra. ')
    elif computer == tesoura:
        print(scissors)
        print('Computador escolheu tesoura! \nComputador ganhou! \nTesoura corta papel!')

elif usuario == tesoura:
    print(scissors)
    print('Você escolheu tesoura')
    if computer == tesoura:
        print(scissors)
        print('Empate! \nComputador escolheu tesoura também.')
    elif computer == pedra:
        print(rock)
        print('Computador escolheu pedra. \nComputador ganhou! \nPedra quebra a tesoura.')
    elif computer == papel:
        print(paper)
        print('Computador escolheu papel! \nVocê ganhou! \nTesoura corta papel!')

else:
    print('Você escolheu o número inválido! \n Execute o jogo novamente.')
    
