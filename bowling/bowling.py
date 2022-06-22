class Game:
    rolls = []

    def roll(self, pin_count):
        self.rolls.append(pin_count)
        return
    def score(self):
        return sum(self.rolls)