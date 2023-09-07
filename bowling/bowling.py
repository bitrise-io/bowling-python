class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, pin_count):
        self.rolls.append(pin_count)

    def score(self):
        return sum(self.rolls)