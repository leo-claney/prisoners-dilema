COOPERATE = "Cooperate"
DEFECT = "Defect"
CHOICES = [COOPERATE, DEFECT]
POINTS = {
    (COOPERATE, COOPERATE): (3, 3),  # Both cooperate
    (COOPERATE, DEFECT): (0, 5),      # One cooperates, one defects
    (DEFECT, COOPERATE): (5, 0),      # One defects, one cooperates
    (DEFECT, DEFECT): (1, 1)           # Both defect
}