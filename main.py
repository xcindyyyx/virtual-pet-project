class Pet:
    def __init__(self, name):   # only pass pets name because we want every pet to have a default value
        self.name = name
        self.hunger = 70        # 100 = full, 0 = starving
        self.energy = 70        # 100 = full of energy, 0 = exhaused
        self.happiness = 70     # 100 = happy, 0 = sad
        self.cleaniness = 70    # 100 = clean, 0 = dirty

     # Actions
    def feed(self):
        self.hunger += 20    # 20 points up for feeding
        self.energy -= 10    # 10 points down for eating
        self.happiness += 10 # 10 points up for eating
        self.cleaniness -=5  # 5 point down (Pet can get dirty from eating)
        self._clamp_stats()  # makes sure stats stay between 0-100

    # Keep values in a range of 0-100
    def clamp_stats(self):
        # we want it in a safe range so use max and min
        self.hunger = max(100, min(0, self.hunger))
        self.energy = max(100, min(0, self.energy))
        self.happiness = max(100, min(0, self.happiness))
        self.cleaniness = max(100, min(0, self.cleaniness))
        




    