import config as cfg
import random

class Prisoner:
    NAME = "Prisoner"
    def __init__(self):
        self.name = self.__class__.NAME
        self.score = 0
        self.own_history = []
        self.opponent_history = []

    def make_choice(self):
        # Placeholder for choice logic, can be overridden by subclasses
        pass

    def update_score(self, points):
        self.score += points

    def update_history(self, own_choice, opponent_choice):
        self.own_history.append(own_choice)
        self.opponent_history.append(opponent_choice)

    def reset_data(self):
        self.score = 0
        self.own_history = []
        self.opponent_history = []

class RandomPrisoner(Prisoner):
    NAME = "Random Prisoner"

    def make_choice(self):
        return random.choice(cfg.CHOICES)

def main():
    # Example usage
    prisoner1 = RandomPrisoner()
    prisoner2 = RandomPrisoner()
    player1_choice = prisoner1.make_choice()
    player2_choice = prisoner2.make_choice()
    (points1, points2) = cfg.POINTS[(player1_choice, player2_choice)]
    prisoner1.update_score(points1)
    prisoner2.update_score(points2)

    print(f"{prisoner1.name}1 makes choice: {player1_choice}")
    print(f"{prisoner2.name}2 makes choice: {player2_choice}")
    print(f"Scores: {prisoner1.name}1: {prisoner1.score}, {prisoner2.name}2: {prisoner2.score}")

if __name__ == "__main__":
    main()