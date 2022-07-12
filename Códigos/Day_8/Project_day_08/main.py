# versão final
from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#FUNÇÃO -----------------------------------------------------
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
# Descriptografar
  if cipher_direction == "decode":
    shift_amount *= -1
# Criptografar -não precisa colocar o elif se for encode 
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
# -------------------------------------------------------------------






# Para entrar no loop e se quiser digitar mais mensagens 
should_end = False
while not should_end: # enquanto não for verdadeiro continua no loop

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26
  #puxa a função
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  # Continuar ?
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True # encerrar verdadeiro
    print("Goodbye")

