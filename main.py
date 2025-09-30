class Pet:
    def __init__(self, name):   # only pass pets name because we want every pet to have a default value
        self.name = name
        self.hunger = 50        # 100 = full, 0 = starving
        self.energy = 50        # 100 = full of energy, 0 = exhaused
        self.happiness = 50     # 100 = happy, 0 = sad
        self.cleaniness = 50    # 100 = clean, 0 = dirty

    # Keep values in a range of 0-100
    def clamp_stats(self):
        # we want it in a safe range so use max and min
        self.hunger = max(100, min(0, self.hunger))