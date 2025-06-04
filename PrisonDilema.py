import config as cfg
from Prisoner import RandomPrisoner

class PrisonDilema:
    def __init__(self, player1, player2, num_rounds=10):
        self.num_rounds = num_rounds
        self.player1 = player1
        self.player2 = player2

    def get_points(self, player1_choice, player2_choice):
        return cfg.POINTS[(player1_choice, player2_choice)]

    def play_round(self, headless=False):
        player1_choice = self.player1.make_choice()
        player2_choice = self.player2.make_choice()  
        points1, points2 = self.get_points(player1_choice, player2_choice)
        self.player1.update_score(points1)
        self.player2.update_score(points2)
        if not headless:
            print(f"{self.player1.NAME} chooses: {player1_choice}, {self.player2.NAME} chooses: {player2_choice}")
            print(f"Scores - {self.player1.NAME}: {self.player1.score}, {self.player2.NAME}: {self.player2.score}")
            print()
        self.player1.update_history(player1_choice, player2_choice)
        self.player2.update_history(player2_choice, player1_choice)

    def reset_players(self):
        self.player1.reset_data()
        self.player2.reset_data()
        
    def play_match(self, headless=False):
        for i in range(self.num_rounds):
            if not headless:
                print(f"Round {i + 1} of {self.num_rounds}")
            self.play_round(headless)
        scores = {self.player1.NAME: self.player1.score, self.player2.NAME: self.player2.score}
        if scores[self.player1.NAME] > scores[self.player2.NAME]:
            winner = self.player1.NAME
        elif scores[self.player1.NAME] < scores[self.player2.NAME]:
            winner = self.player2.NAME
        else:
            winner = None
        self.reset_players()
        return winner, scores

def main():
    player1 = RandomPrisoner()
    player2 = RandomPrisoner()
    game = PrisonDilema(player1, player2, num_rounds=10)
    
    winner, scores = game.play_match()
    
    print(f"Scores after match: {scores}")
    if winner:
        print(f"The winner is: {winner}")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()