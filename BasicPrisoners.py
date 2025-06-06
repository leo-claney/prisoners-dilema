import config as cfg
from Prisoner import Prisoner
import random

class RandomPrisoner(Prisoner):
    NAME = "Random Prisoner"

    def make_choice(self):
        return random.choice(cfg.CHOICES)

class CooperatePrisoner(Prisoner):
    NAME = "Cooperate Prisoner"

    def make_choice(self):
        return cfg.COOPERATE

class DefectPrisoner(Prisoner):
    NAME = "Defect Prisoner"

    def make_choice(self):
        return cfg.DEFECT

class TitForTatPrisoner(Prisoner):
    NAME = "Tit for Tat"

    def make_choice(self):
        if len(self.own_history) == 0 or self.opponent_history[-1] == cfg.COOPERATE:
            return cfg.COOPERATE
        return cfg.DEFECT

class VengefulPrisoner(Prisoner):
    NAME = "Vengeful Prisoner"

    def make_choice(self):
        if len(self.own_history) == 0 or cfg.DEFECT not in self.opponent_history:
            return cfg.COOPERATE
        return cfg.DEFECT