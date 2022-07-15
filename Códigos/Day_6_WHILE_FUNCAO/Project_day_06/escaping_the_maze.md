# Programa para o robô chegar até a bandeira
# para executar o código acesse o link 
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

## função para virar a direita
def turn_right():
    turn_left()
    turn_left()
    turn_left()

## para não entrar no loop infinito    
while front_is_clear():
    move()
turn_left()

## enquanto não chegar a bandeira ele vai executar os seguintes algoritmos 
while not at_goal():
    if right_is_clear():
        turn_right()    
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()