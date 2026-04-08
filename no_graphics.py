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
    
def calculate_winning_hand(hands):
    values = []
    blackjack_counter = 0
    for i in hands:
        if i.hand_value() == "Bust":
            continue
        if i.hand_value() == "Blackjack":
            blackjack_counter += 1
        values.append([i.name, i.hand_value()])

    if len(values) == 0:
        return "Dealer Wins"

            
    if any(v[1] == "Blackjack" for v in values):
        for j in range(len(values)):
            if values[j][1] == "Blackjack" and blackjack_counter == 1:
                return f"{values[j][0]} Wins with Blackjack"
            
        if blackjack_counter == len(hands):
            return "Push/Draw"
        
        if blackjack_counter > 1 and blackjack_counter < len(hands):
            for i, sublist in enumerate(values):
                if "Blackjack" in sublist:
                    if ["Dealer", "Blackjack"] in values:
                        return f"Push for {values[i][0]} win, the rest lose"
                    else:
                        return f"{values[i][0]} have Blackjack"
                
                else:
                    pass
    else:
        highest_to_smallest = sorted(values, key=lambda x: x[1], reverse=True)
        return f"{highest_to_smallest[0][0]}, Wins"

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
        print("\n\n", dealer.cards[1], "\n\n", "you:   ", you.cards)

        if Dealer_value == "Blackjack" and not Player_value == "Blackjack":
            return "Dealer wins, you lose"

        if Dealer_value == "Blackjack" and Player_value == "Blackjack":
            return "PUSH"

        if not Dealer_value == "Blackjack" and Player_value == "Blackjack":
            return "You WIn"
        
        run = True
        while run:
       
            decision = input("Hit or Stay?  ").lower()
            if decision == "hit":
                you.hit(deck)
                print("\n\n", dealer.cards[1], "\n\n", "you:   ", you.cards)
                if you.hand_value() == "Bust":
                    return "Dealer wins, you lose"
            else:
                run = False
        
        while isinstance(Dealer_value, int) and Dealer_value < 17:
            dealer.hit(deck)
            Dealer_value = dealer.hand_value()

        print("\n\n", dealer.cards, "\n\n", "you:   ", you.cards)

        return calculate_winning_hand(players)
    
if __name__ == "__main__":
        playing = True
        while playing:
            play = input("Do you want to play BlackJack?   ").lower()
            if play == "yes":
                print(main())
            else:
                play = False
                break