"""Black Jack game"""

import random

COLORS = {'♠', '♦', '♥', '♣'}
FIGURES = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}

class Table:
    """main class in game where are all interactions
    """
    def __init__(self, players, dealer, deck):
        self.players = players
        self.dealer = dealer
        self.deck = deck

    def deal_cards(self):
        """dealing 2 cards for all players (include dealer)
        """
        for _ in range(2):
            for player in self.players:
                self.hit_card(player)
            self.hit_card(self.dealer)

    def hit_card(self, player):
        """dealing card for player

        Args:
            player (object class Player): player who take card
        """
        player.cards_on_hand.append(self.deck.give_card())

    def show(self):
        """showing/refreshing cards on table
        """
        print()
        print('---'*8)
        print(self.dealer, end=' ma ')
        print('['+str(self.dealer.cards_on_hand[0]) + ', **]')
        print()
        for player in self.players:
            print(player, end=' ma ')
            print(player.cards_on_hand, end='    ')


class Player:
    """player or dealer
    """
    def __init__(self, name) -> None:
        self.name = name
        self.cards_on_hand = []
        self.cards_value = 0
        self.cash = 0

    def count_cards(self):
        """counting cards on players hand

        Returns:
            int: cards value
        """
        for card in self.cards_on_hand:
            self.cards_value += card.check_value()
        return self.cards_value

    def __str__(self):
        return self.name


class Deck:
    """deck of cards
    """
    def __init__(self, number_of_decks) -> None:
        self.number_of_decks = number_of_decks
        self.cards = self.create_deck(self.number_of_decks)
        self.shuffle()

    @staticmethod
    def create_deck(number_of_decks):
        """creating table's deck from one deck of 52 cards or more
            to create use 13 figure and 4 colors of playing cards

        Args:
            number_of_decks (int):numbers decks of cards

        Returns:
            list: deck with cards
        """
        cards = []
        i = 0
        while i < number_of_decks:
            for figure in FIGURES:
                for color in COLORS:
                    card = Card(figure, color)
                    cards.append(card)
            i += 1
        return cards

    def shuffle(self):
        """shuffling card in deck
        """
        random.shuffle(self.cards)

    def give_card(self):
        """return one card from deck and remove it from deck

        Returns:
            object class Card: card taken from deck
        """
        return self.cards.pop(0)

    # def __repr__(self):
    #     return self.cards


class Card:
    """one card with figure, color and value
    """
    def __init__(self, figure, color) -> None:
        self.figure = figure
        self.color = color
        self.value = 0

    def check_value(self):
        """checking value card in black jack

        Returns:
            int: value of card
        """
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
        if i == players_number:
            break
        i += 1
    dealer = Player('KRUPIER')
    number_of_decks = int(input('Podaj liczbę talii kart jaką chcesz grać: '))
    deck = Deck(number_of_decks)
    table = Table(players, dealer, deck)
    table.deal_cards()
    table.show()

    # player.take_card(deck.give_card())
    # print(f'{player} has a card: {player.cards_on_hand[0]}')
