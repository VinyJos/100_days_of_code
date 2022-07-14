from art import logo
import os
print(logo)
print('Welcome to the secret auction program.')

list_offers = []

# PARA LIMPAR O CONSOLE
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



# SALVANDO A ENTRADA DE DADOS NO DICIONÁRIO
def auction(name, bid):
    list_offers.append({
        'name_user_offer': name, 
        'offer_value': bid
    })

    # print(list_offers)

# IMPRESSÃO DO RESULTADO FINAL
def auction_result():
    # para dar certo if, tem que comparar dicionario com dicionario 
    highest_auction_bid = {'offer_value':0}
    for offer in list_offers:
        dice = offer['offer_value']
        if dice > highest_auction_bid['offer_value']:
            highest_auction_bid = offer
    print(f"The winner is {highest_auction_bid['name_user_offer']} with a bid of ${highest_auction_bid['offer_value']:.2f}")


# LOOP PARA CONTINUAR DIGITANDO OS LANCES SIM/NÃO
end_offers = False
while not end_offers:
    name_user = input('What is your name?: ').title()
    bid_user = eval(input("What's your bid?: $"))

    auction(name=name_user, bid=bid_user )
    end_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n" ).lower()
    clearConsole()
    # CASO NÃO CONTINUE
    if end_continue == 'no':
        end_offers = True
        clearConsole()
        auction_result()