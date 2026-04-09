import random

#classes

class Deck:

    def __init__(self):

        self.deck = []
    def build_deck(self):
        ranks = ["Ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "Jack", "Queen", "King"]
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        card_values = {"Ace":11,"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "Jack":10, "Queen":10, "King":10}
        for i in ranks:
            for j in suits:
                self.deck.append(Card(i, j, card_values[i]))
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def give_card(self):
        return self.deck.pop()

    
class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_initial_cards(self, deck):
        for _ in range(2):
            self.cards.append(deck.give_card())
        return self.cards
    
    def hit(self, deck):
        self.cards.append(deck.give_card())
    
    def hand_value(self):
        values = []
        ace_counter = 0
        index = 0
        for i in self.cards:
            rank = i.rank
            if rank == "Ace":
                ace_counter += 1
            values.append(i.value)
            index += 1
        total = sum(values)
        self.total = total
        while total > 21 and ace_counter > 0:
            total -= 10
            ace_counter -= 1

        if total > 21:
            return "Bust"
        
        if total == 21 and len(self.cards) == 2:
            return "Blackjack"
        
        return total

#final function to figure out the winner

def calculate_winning_hand(player, dealer):
    player_value = player.hand_value()
    dealer_value = dealer.hand_value()
    if isinstance(player_value, int) and isinstance(dealer_value, int):
        if player_value > dealer_value:
            return "You win"
        if player_value < dealer_value:
            return "Dealer wins, you lose"
        if player_value == dealer_value:
            return "Push"
    
    if dealer_value == "Bust":
        return "You win"
    
    if player_value == "Bust":
        return "Dealer wins, you lose"

#game loop and funtion

def main():
    deck = Deck()
    deck.build_deck()
    deck.shuffle()
    you = Hand("You")
    dealer = Hand("Dealer")
    players = [you, dealer]
    while True:
        for player in players:
            player.get_initial_cards(deck)
        
        Dealer_value = dealer.hand_value()
        Player_value = you.hand_value()

        if Dealer_value == "Blackjack" and not Player_value == "Blackjack":
            print("---------------------------------------------------------")
            print("Dealer:", dealer.cards, "\n\n", "you:", you.cards, f" - {you.hand_value()}")
            print("---------------------------------------------------------")
            return "Dealer wins, you lose"
        else:
            print("---------------------------------------------------------")
            print("Dealer:", dealer.cards[0], "\n\n", "you:", you.cards, f" - {you.hand_value()}")
            print("---------------------------------------------------------")

        if Dealer_value == "Blackjack" and Player_value == "Blackjack":
            return "Push"

        if not Dealer_value == "Blackjack" and Player_value == "Blackjack":
            return "You WIn"
        
        run = True
        while run:
       
            decision = input("Hit or Stay?  ").lower()
            if decision == "hit":
                you.hit(deck)
                print("---------------------------------------------------------")
                print("Dealer:",  dealer.cards[0], "\n\n", "you:", you.cards, f" - {you.hand_value()}")
                print("---------------------------------------------------------")
                if you.hand_value() == "Bust":
                    return "Dealer wins, you lose"
            else:
                run = False
        
        while isinstance(Dealer_value, int) and Dealer_value < 17:
            dealer.hit(deck)
            Dealer_value = dealer.hand_value()
        print("---------------------------------------------------------")
        print("Dealer:", dealer.cards, f" - {dealer.hand_value()}", "\n\n", "you:", you.cards, f" - {you.hand_value()}")
        print("---------------------------------------------------------")

        return calculate_winning_hand(you, dealer)
    
#runs script

if __name__ == "__main__":
        playing = True
        play_counter = 0
        while playing:
            if play_counter == 0:
                play = input("Do you want to play BlackJack?   ").lower()
                if play == "yes":
                    play_counter += 1
                    print(main())
                else:
                    play = False
                    break
            elif play_counter > 0:
                play = input("Do you want to play BlackJack again?   ").lower()
                if play == "yes":
                    play_counter += 1
                    print(main())
                else:
                    play = False
                    break