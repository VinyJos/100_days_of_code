# Esse é um algoritmo do jogo da forca 
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# O computador escolhe uma palavra da lista
print('Bem vindo ao jogo forca!')
word_list = ['cavalo', 'cachorro', 'hotdog', 'stronogof', 'pastel', 'cerveja']
chosen_word = random.choice(word_list)


display = []
word_length = len(chosen_word)

lives = 6
# Cria os espaços em branco
for letter in chosen_word: # ou pode fazer com o range (igual abaixo)
    display += '_'
print(display)

end_of_game = False # atribuiu começando falso para entrar no while

while not end_of_game: #(enquanto não falso)
    guess = input('Guess a letter:').lower()

    for position in range(word_length):
        letter = chosen_word[position] # pegou a posição da palavra que está na variável chosen_word e jogou na variável letter
        
        #se a palavra que esta na variável letter for igual da palavra que o usuário digitou, vai pegar a posição do momento e jogar na variável display
        if letter == guess:
            display[position] = letter
    # SE ERRAR A LETRA FAZ A SEGUINTE FUNÇÃO
    if guess not in chosen_word: # (se a letra não está em chosen_word)
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose.')
    
    print(f"{' '.join(display)}") # para tirar aspas e colchetes da lista
    
    # SE ACERTAR TUDO 
    if '_' not in display: # (se '_' não está no display)
        end_of_game = True
        print('You win.')

    print(stages[lives])