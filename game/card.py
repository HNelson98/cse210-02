import random

class Card():
    """A card with a number on it within the range 1-13
    
    The responisbility of the card is to keep track of the value face up card.

    Attributes:
        value (int): The number on the face up card
    """
    def __init__(self):
        """Constructs a new instance of Card with a value attribue

        Args: 
            self (Card): an instance of Card
        """
        self.value = 0

    def draw_card(self):
        """Generates a new random value

        Args: 
            self (Card): an instance of Card
        """
        self.value = random.randint(1,13)
