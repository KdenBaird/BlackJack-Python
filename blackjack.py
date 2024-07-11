import random
import sys

def reset_deck():
    return create_deck()

def main():

    while True:
        print("Blackjack Menu: ")
        print("1. Read rules ")
        print("2. Start game ")
        print("3. Exit ")
        
        user_choice = input("Please select an option: ")

        if user_choice == "1":
            read_rules()
        
        elif user_choice == "2":
            start_game()

        elif user_choice == "3":
            print("Thanks for playing BlackJack!")
            sys.exit()

        else:
            print("Invalid choice. Please enter a valid option.")
            main()

def read_rules():
    
    print("\nRules of Blackjack:\n")
    print("-- The goal is to get as close to 21 as possible without going over.")
    print("-- Numbered cards are worth their face value, face cards are worth 10, ACES ARE ALWAYS WORTH 11 PTS.")
    print("-- The dealer gives two cards to each player and keeps one card hidden.")
    print("-- Players can 'hit' to receive an additional card or 'stand' to stop receiving cards.")
    print("-- If a player's total exceeds 21, they bust and lose the game.")
    print("-- If a player stands, the dealer reveals their hidden card and hits until their total is at least 17.")
    print("-- The player closest to 21 without going over wins.\n")

# Function to start the game
def start_game():

    deck = create_deck()
    player_hand = []
    dealer_hand = []

    # Give two cards to the player the"(2)"" iterates through the loop twice.
    for _ in range(2):
        card = random.choice(deck)
        player_hand.append(card)
        deck.remove(card)

    # Give two cards to the dealer "(2)" indicates that the loop is iterated twice.
    for _ in range(2):
        card = random.choice(deck)
        dealer_hand.append(card)
        deck.remove(card)

    print(f'\nYour total is: {calculate_total(player_hand)}')
    #total_hand = int(dealer_hand[0]) + int(dealer_hand[1])
    print(f"Your hand: {player_hand}" )
   
    dealers_total = calculate_dealers_total(dealer_hand)
    print(f"Dealer's top card: {dealer_hand[0]}\n")
    user_total = calculate_total(player_hand)

    if calculate_total(player_hand) == 21:
        print(f'Your total is: {user_total}')
        stand(dealer_hand, player_hand, deck, dealers_total, user_total)
        
    user_choice = 0 
    while user_choice != "2":
        user_choice = input("Please enter '1' to hit or '2' to stand: ")
        
        if user_choice == "1":
            card = hit_me(deck)
            player_hand.append(card)
            deck.remove(card)
            user_total = calculate_dealers_total(player_hand)
            print(f'\nYour total is: {user_total}')
            print(f"Your hand: {player_hand}" )
                    
            if calculate_total(player_hand) > 21:
                print(f'\nYou went over 21. Your total was: {calculate_total(player_hand)}. Better luck next time!\n')
                break

    if user_choice == "2":
        print(f"\nDealer's total is: {dealers_total}")
        print(f"Dealer's hand is: {dealer_hand}")
        stand(dealer_hand, player_hand, deck, dealers_total, user_total)
        print(f"\nDealer's total is: {dealers_total}")
        print(f"Dealer's hand is: {dealer_hand}")
        stand(dealer_hand, player_hand, deck, dealers_total, user_total)
                     
# Function to create a deck of cards
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(number, suit) for number in numbers for suit in suits]
    return deck
  
def hit_me(deck):
    for _ in range(1):
        card = random.choice(deck)
        return card

def dealer_hit(deck):
    for _ in range(1):
        card = random.choice(deck)
        return card

def calculate_total(userhand):
    total = 0
    for card in userhand:
        rank = card[0]  # Accessing the rank from the tuple
        if rank in ['Jack', 'Queen', 'King']:
            total += 10
        elif rank == 'Ace':
            total += 11
        else:
            total += int(rank) # Convert rank to integer value
    
    return total

def calculate_dealers_total(dealer_hand):
    total = 0
    
    for card in dealer_hand:
        rank = card[0]  # Accessing the rank from the tuple
        if rank in ['Jack', 'Queen', 'King']:
            total += 10
        elif rank == 'Ace':
            total += 11
        else:
            total += int(rank) # Convert rank to integer value
    return total

def stand(dealerhand, userhand, card_deck, dealers_total, users_total):

    dealer_hand = dealerhand
    player_hand = userhand
    deck = card_deck
    dealers_total = calculate_dealers_total(dealer_hand)

    if dealers_total == users_total:
        print("You and the dealer both have the same amount you tied!\n")
        main()
    while dealers_total < 17:
        print("Dealer draws a card.")
        print('**REMINDER: Dealer stands on anything more than 16.\n')
        card = dealer_hit(deck)
        dealer_hand.append(card)
        deck.remove(card)
        dealers_total = calculate_dealers_total(dealer_hand)
        print(f"Dealers total is: {dealers_total}")
        print(f"Dealer's hand is: {dealerhand}")

    if dealers_total > 21:
        print("Dealer busts! You win!\n")
        main()

    if dealers_total == users_total:
        print("You and the dealer both have the same amount you tied!\n")
        main()
        
    if users_total > dealers_total:
        print("You win!\n")
        main()

    if dealers_total > users_total:
        print("You lose!\n")
        main()

if __name__ == "__main__":
    main()