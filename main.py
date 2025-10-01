class Pet:
    def __init__(self, name):   # only pass pets name because we want every pet to have a default value
        self.name = name
        self.hunger = 70        # 100 = full, 0 = starving
        self.energy = 70        # 100 = full of energy, 0 = exhaused
        self.happiness = 70     # 100 = happy, 0 = sad
        self.cleanliness = 70    # 100 = clean, 0 = dirty

     # Actions
    def feed(self):
        self.hunger += 20    # 20 points up for feeding
        self.energy -= 10    # 10 points down for eating
        self.happiness += 10 # 10 points up for eating
        self.cleanliness -=5  # 5 point down (Pet can get dirty from eating)
        self.clamp_stats()   # makes sure stats stay between 0-100

    def play(self):
        self.hunger -= 20    # 20 points down for playing
        self.energy -= 30    # 30 points down for playing
        self.happiness += 40 # 40 points up for playing
        self.cleanliness -=35 # 35 point down for playing
        self.clamp_stats()   # makes sure stats stay between 0-100

    def bathe(self):
        self.hunger -= 5     # 5 points down for bathing
        self.energy -= 30    # 30 points down for bathing
        self.happiness += 40 # 40 points up for bathing
        self.cleanliness +=35 # 35 point up for bathing
        self.clamp_stats()   # makes sure stats stay between 0-100

    def status(self):
        return (f"Hunger: {self.hunger} \n"
                f"Energy: {self.energy} \n"
                f"Happiness: {self.happiness} \n"
                f"Cleanliness: {self.cleanliness} \n")
    
    # Keep values in a range of 0-100
    def clamp_stats(self):
        # we want it in a safe range so use max and min
        self.hunger = max(0, min(100, self.hunger))
        self.energy = max(0, min(100, self.energy))
        self.happiness = max(0, min(100, self.happiness))
        self.cleanliness = max(0, min(100, self.cleanliness))
        
if __name__ == "__main__":
    pet = Pet("Pancho") # Pass a name into the parameter 
    print(f"\nHere is your default pet: {pet.name}")
    print(f"By default, all stats start at 70.\n")

    while True:
        action = input("Choose: feed, play, bathe, or quit: ").lower()

        match action:
            case "feed":
                pet.feed()
                print(f"-- {pet.name}'s stats --")
                print(pet.status())
                # if pet.hunger == 0:
                #     print(f"{pet.name} has passed away from hunger :(\n")
                #     break
            case "play":
                pet.play()
                print(f"-- {pet.name}'s stats --")
                print(pet.status())
                continue
            case "bathe":
                pet.bathe()
                print(f"-- {pet.name}'s stats --")
                print(pet.status())
                continue
            case "quit":
                print("Goodbye!\n")
                break
            case _:
                print("Invalid action!")

    

    print(f"-- {pet.name}'s Final Stats --")
    print(pet.status())




    