import os, sys, pydealer
from pyfiglet import Figlet

f = Figlet(font="larry3d")

blackjack_ranks = {
    "values": {
        "Ace": 11,
        "King": 10,
        "Queen": 10,
        "Jack": 10,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }
}

def main():
    while True:
        print(f.renderText("BlackJack"))
        print("PLAY[1]\nEXIT[2]")
        action = str(input(": ").strip().lower())
        clear_screen()
        
        if action == "1":
            play_game()        
        
        elif action == "2":
            sys.exit("Closing...")
            
        else:
            print("Choose a valid option.")

def play_game():
    global player_hand, dealer_hand, player_dealt_cards, dealer_dealt_cards, deck
    
    deck = pydealer.Deck(ranks=blackjack_ranks)
    deck.shuffle()
    
    player_hand = pydealer.Stack()
    player_dealt_cards = deck.deal(2)
    player_hand.add(player_dealt_cards)

    dealer_hand = pydealer.Stack()
    dealer_dealt_cards = deck.deal(2)
    dealer_hand.add(dealer_dealt_cards)

    points_dealer = rank_sum(dealer_dealt_cards)
    points_player = rank_sum(player_dealt_cards)

    while True: 
        print(f"Dealer points: {rank_sum([dealer_dealt_cards[0]])}")
        draw_hand([dealer_hand[0]])
        
        print(f"Player Points: {points_player}")
        draw_hand(player_hand)
        
        if points_player == 21 and points_dealer == 21:
            print("Both have Blackjack!")
            print(f.renderText("It's a draw!"))
            ask_to_play_again()
        elif points_player == 21:
            clear_screen()
            print(f"Dealer points: {rank_sum([dealer_dealt_cards[0]])}")
            draw_hand([dealer_hand[0]])
            print(points_player)
            draw_hand(player_hand)
            print("You got a Blackjack!")
            
        
        
        print("Do you want to hit or stand?\nHIT[1]\nSTAND[2]")
        action = str(input(": ").strip().lower())
        clear_screen()
        
        if action == "1":
            new_card = deck.deal(1)[0]
            player_hand.add(new_card)
            points_player = rank_sum(player_hand)
        
            print(f"You drew a {new_card}")
            
            if points_player > 21:
                print(f"Player points: {points_player}")
                draw_hand(player_hand)
                print("You busted!")
                print(f.renderText("Dealer wins!"))
                ask_to_play_again()
                
            elif points_player == 21:
                print(f"Player points: {points_player}")
                draw_hand(player_hand)
                print("You got a BlackJack!")
                
            
        elif action == "2":
            while points_dealer < 17:
                new_card = deck.deal(1)[0]
                dealer_hand.add(new_card)
                points_dealer = rank_sum(dealer_hand)
                print(f"Dealer drew a {new_card}")
                    
            if points_dealer > 21:
                print(f"Dealer points: {points_dealer}")
                draw_hand(dealer_hand)
                print("Dealer busted!")
                print(f.renderText("You win!"))
                ask_to_play_again()
              
            elif points_dealer == 21:
                print(f"Dealer points: {points_dealer}")
                draw_hand(dealer_hand)
                print("The dealer got a Blackjack")
                print(compare_points(points_player, points_dealer))
                ask_to_play_again()
            
            else:
                print(f"Dealer points: {points_dealer}")
                draw_hand(dealer_hand)
                print(f"Player points: {points_player}")
                draw_hand(player_hand)
                print(compare_points(points_player, points_dealer))
                ask_to_play_again()

def draw_hand(hand):
    card_lines = [""] * 7
          
    for card in hand:
        rank = card.value
        suit = card.suit
        card_rank = convert_rank(rank)
        card_suit = convert_suit(suit)
        card_visual = get_card_lines(card_rank, card_suit)
        
        for i in range(7):
            card_lines[i] += card_visual[i] + "  "
    
    for line in card_lines:
        print(line)

def get_card_lines(rank, suit):
    card_lines = [
        "┌─────────┐",
        f"│{rank: <2}       │" if rank != "10" else f"│{rank}       │",  
        "│         │",
        f"│    {suit}    │",
        "│         │",
        f"│       {rank: >2}│" if rank != "10" else f"│       {rank}│",  
        "└─────────┘"
    ]
    
    return card_lines


def convert_suit(suit):
    match suit:
        case "Diamonds":
            return "♦"
        case "Hearts":
            return "♥"
        case "Spades":
            return "♠"
        case "Clubs":
            return "♣"

def convert_rank(rank):
    match rank:
        case "Ace":
            return "A"
        case "King":
            return "K"
        case "Queen":
            return "Q"
        case "Jack":
            return "J"
        case _:
            return rank

def rank_sum(hand):
    values = []
    num_aces = 0
    
    for card in hand:
        if card.value in ["King", "Queen", "Jack"]:
            value = 10
            values.append(value)
        elif card.value == "Ace":
            num_aces += 1
            value = 11
            values.append(value)
        else:
            values.append(int(card.value))
    
    while sum(values) > 21 and num_aces > 0:
        values[values.index(11)] = 1
        num_aces -= 1
        
    return sum(values)

def compare_points(points_player, points_dealer):
    if points_player > points_dealer:
        result = f.renderText("You win!")
        
    elif points_dealer > points_player:
        result = f.renderText("Dealer wins!")
        
    else:
        result = f.renderText("It's a draw!")
    
    return result

def ask_to_play_again():
    while True:
        option = str(input("Try again?\nYes[1]\nNo[2]\n: ").lower().strip())
        clear_screen()
        
        if option == "1":
            play_game()
        elif option == "2":
            sys.exit("Closing game...")
        else:
            print("Choose a valid option")

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()
