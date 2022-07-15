from art import logo


# Funções
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

# Dicionario
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))

  # Para
  for symbol in operations:
    print(symbol)

  should_continue = True

  #Enquanto não falso
  while should_continue:

    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    # If com input
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()