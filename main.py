"""Black Jack game"""

import random

from numpy import number

COLORS = {'♠', '♦', '♥', '♣'}
FIGURES = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}

class Table:
    def __init__(self, players, dealer, deck):
        self.players = players
        self.dealer = dealer
        self.deck = deck
    
    def deal_cards(self):
        for _ in range(2):
            for player in self.players:
                self.hit_card(player)
            self.hit_card(self.dealer)
    
    def hit_card(self, player):
        player.cards_on_hand.append(self.deck.give_card())
    
    def show(self):
        print()
        print('---'*8)
        print(self.dealer, end=' ma ')
        print('['+str(self.dealer.cards_on_hand[0]) + ', **]') 
        print()
        for player in self.players:
            print(player, end=' ma ')
            print(player.cards_on_hand, end='    ')


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.cards_on_hand = []
        self.cash = 0
    
    def take_card(self, card):
        self.cards_on_hand.append(card)

    def __str__(self):
        return self.name
    
            
class Deck:
    def __init__(self, number_of_decks) -> None:
        self.number_of_decks = number_of_decks
        self.cards = self.create_deck()
        self.shuffle()
    
    def create_deck(self):
        cards = []
        i = 0
        while i < self.number_of_decks:
            for figure in FIGURES:
                for color in COLORS:
                    card = Card(figure, color)
                    cards.append(card)
            i += 1
        return cards

    def shuffle(self):
        random.shuffle(self.cards)
    
    def give_card(self):
        return self.cards.pop(0)

    # def __repr__(self):
    #     return self.cards

class Card:
    def __init__(self, figure, color) -> None:
        self.figure = figure
        self.color = color
        self.value = 0
    
    def check_value(self):
        try:
            self.value = int(self.figure)
        except ValueError:
            if self.figure == 'A':
                self.value = 11
            else:
                self.value = 10
        return self.value

    def __str__(self):
        return str(self.figure + self.color)

    def __repr__(self):
        return str(self.figure + self.color)


if __name__ == "__main__":
    print()
    print('**************************')
    print('*  Zagrajmy w BlackJack  *')
    print('**************************')
    print()
    players_number = int(input('Podaj liczbę graczy: '))
    players = []
    i = 1
    while True:
        name = input(f"Podaj imię gracza nr {i}: ")
        player = Player(name)
        players.append(player)
        if i == players_number: break
        i += 1
    dealer = Player('KRUPIER')
    number_of_decks = int(input('Podaj liczbę talii kart jaką chcesz grać: '))
    deck = Deck(number_of_decks)
    table = Table(players, dealer, deck)
    table.deal_cards()
    table.show()
    
    
    
  
    # player.take_card(deck.give_card())
    # print(f'{player} has a card: {player.cards_on_hand[0]}')


