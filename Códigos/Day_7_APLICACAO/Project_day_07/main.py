# Esse é um algoritmo do jogo da forca 
import random
from hangman_word import word_list, clearConsole
from hangman_art import stages,  logo


# O computador escolhe uma palavra da lista
print('Welcome to the hangman game!')
print(logo)
chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)
lives = 6

# Cria os espaços em branco
for letter in chosen_word: # ou pode fazer com o range (igual abaixo)
    display += '_'

end_of_game = False # atribuiu começando falso para entrar no while

while not end_of_game: #(enquanto não falso)
    guess = input('Guess a letter: ').lower()
    #para limpar o console assim que executa e digite a palavra
    clearConsole()

    if guess in display: 
      print(f"You've already guessed {guess}")


    for position in range(word_length):
        letter = chosen_word[position] # pegou a posição da palavra que está na variável chosen_word e jogou na variável letter
        
        #se a palavra que esta na variável letter for igual da palavra que o usuário digitou, vai pegar a posição do momento e jogar na variável display
        if letter == guess:
            display[position] = letter
    # SE ERRAR A LETRA FAZ A SEGUINTE FUNÇÃO
    if guess not in chosen_word: # (se a letra não está em chosen_word)
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
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