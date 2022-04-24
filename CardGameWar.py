#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards
# Suite for Hearts, Diamonds, Spades and Clubs
# Ranks for the numbering of the cards
# split() with no argument splits the string into a list based on spaces
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class which will create a deck of cards to initiate and use 
    to play. This Deck list of cards can be split in half to give to the players.
    """

    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    '''
    This is the Hand class where players can add or remove cards from their hand.
    '''

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    '''
    This is the Player class which defines the checks for the scenarios of the 
    game. In this class there are 3 main functions which are checks to play, 
    remove cards based on a 'war', and checks to see if players still have cards
    left to continue playing with
    '''

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Returns True if player still has cards
        """
        return len(self.hand.cards) != 0


# Game Start!!!
print("Welcome to the classic card game War!")

# Initialize deck and use split function to split in half (after shuffling)
d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

# Automatically create computer and ask user for their screen name
comp = Player("computer", Hand(half1))
name = input("Please enter your name: ")
user = Player(name, Hand(half2))

# Initialize the round counts
total_rounds = 0
war_count = 0

# Game loop
while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Let's begin a new round!")
    print("Here are is the leaderbords: ")
    print(user.name+" count: "+str(len(user.hand.cards)))
    print(comp.name+" count: "+str(len(comp.hand.cards)))
    print("Both players play a card!")
    print('\n')

    # Table cards represented as list
    table_cards = []

    # Both comp and user play cards
    c_card = comp.play_card()
    p_card = user.play_card()

    # Append cards to the table_cards list
    table_cards.append(c_card)
    table_cards.append(p_card)

    # Check for War
    if c_card[1] == p_card[1]:
        war_count += 1
        print("Cards Match! Time for War!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        # Play cards
        c_card = comp.play_card()
        p_card = user.play_card()

        # Add to table_cards
        table_cards.append(c_card)
        table_cards.append(p_card)

        # Check to see who won based on card rank and then adds the winning cards to their hand
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, they win this war!")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, they win this war!")
            comp.hand.add(table_cards)

    else:
        # Check to see who won based on card rank and then adds the winning cards to their hand
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, they win this war!")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, they win this war!")
            comp.hand.add(table_cards)

print("Awesome game! Total number of rounds: "+str(total_rounds))
print("Total number of wars: "+str(war_count))
