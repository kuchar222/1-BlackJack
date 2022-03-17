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
        self.show()

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
        if self.dealer.passed is False:
            print('['+str(self.dealer.cards_on_hand[0]) + ', **]')
        else:
            print(self.dealer.cards_on_hand)
        print()
        for player in self.players:
            print(player, end=' ma ')
            print(player.cards_on_hand, end='    ')
        print()
        print('---'*8)

    def ask_for_card(self):
        """asking player for hit card or pass
            and checking his points

        Returns:
            bool: True if is any player who didn't passed
        """
        end = False
        for player in self.players:
            if player.passed is False:
                end = True
                if input(f'{player} czy chcesz dobrać kartę? (t/n): ').lower() == 't':
                    self.hit_card(player)
                    self.show()
                    if player.count_cards() == 21:
                        print(f'{player} masz 21 punktów, W Y G R Y W A S Z ! ! !')
                        player.passed = True
                    elif player.count_cards() > 21:
                        print(f'{player} masz ponad 21 punktów, to koniec gry dla Ciebie')
                        player.passed = True
                else:
                    player.passed = True
        return end


class Player:
    """player or dealer
    """
    def __init__(self, name) -> None:
        self.name = name
        self.cards_on_hand = []
        self.cards_value = 0
        self.passed = False
        self.cash = 0

    def count_cards(self):
        """counting cards on players hand

        Returns:
            int: cards value
        """
        self.cards_value = sum(card.value for card in self.cards_on_hand)
        # player has 2 aces his point should be 21
        if self.cards_value == 22 and len(self.cards_on_hand) == 2:
            self.cards_value = 21
        # count 1 point for Ace when sum of all cards is more than 21
        elif self.cards_value > 21:
            for card in self.cards_on_hand:
                if card.value == 11:
                    self.cards_value -= 10
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


class Card:
    """one card with figure, color and value
    """
    def __init__(self, figure, color) -> None:
        self.figure = figure
        self.color = color
        self.value = self.check_value()

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
    while True:
        if table.ask_for_card() is False:
            break
    table.dealer.passed = True
    table.show()
    while True:
        if table.dealer.count_cards() < 17:
            table.hit_card(dealer)
        else:
            break
    table.show()
    if table.dealer.cards_value > 21:
        print('Krupier przekroczył 21 punktów, ')
        for player in table.players:
            if player.count_cards() < 22:
                print(f'{player} WYGRYWASZ')
    else:
        for player in table.players:
            if player.count_cards() - table.dealer.cards_value > 0 and player.count_cards() < 21:
                print(f'{player} wygrywasz z Krupierem')
            else:
                print(f'{player} Krupier wygrał z Tobą')
