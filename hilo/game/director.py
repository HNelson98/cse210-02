from game.card import Card
#Director Behaviors check guess. check next card. display next card. 
# check score. ask if player wants to play again.

# Data dummy
score = 300
first_card = 1
next_card = 3

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
    """
print(f"\nThe card is: {first_card}")

higher_or_lower = input("Higher or lower? [h/l] ").lower

print(f"Your next card was: {next_card}")

def check_guess(higher_or_lower, score, first_card, next_card):
    if higher_or_lower == "h":
        if first_card > next_card:
            player_earns_points(score)
        else: player_losses_points(score)
    elif higher_or_lower == "l":
        if first_card < next_card:
            player_earns_points(score)
        else: player_losses_points(score)

def player_losses_points(score):
    score -= 75

def player_earns_points(score):   
    score += 100