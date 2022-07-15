#CALCULADORA SIMPLESMENTE PARA MOSTRAR O  DEF DICIONARIO E FOR 
# SE NÃO PODERIA SER FEITO DE UMA MANEIRA MAIS SIMPLES


# Adição
def add(n1, n2):
    return n1 + n2
# Subtração
def sub(n1, n2):
    return n1 - n2
# Multiplicação
def mult(n1, n2):
    return n1 * n2
# Divisão
def div(n1, n2):
    return n1 / n2

list_calculator = {
    '+': add, 
    '-': sub, 
    '*': mult, 
    '/': div
    } 

num1 = int(input("What's the first number ?: "))

for operator in list_calculator:
    print(operator)
what_operator = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number ?: "))
# puxa o caractere da lista, entra no def e joga os dois números, depois faz a conta e retorna
answer = list_calculator[what_operator](num1, num2) # combinação de entrada, lista e função

print(f"{num1} {what_operator} {num2} = {answer}")
       