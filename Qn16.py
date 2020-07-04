class Mario:
    # Constructor
    def __init__(self, Lives, Coins, Multiplier):
        self.Lives = Lives
        self.Coins = Coins
        self.Multiplier = Multiplier

    # Coins collect
    def coins_collect(self, coin):
        self.Coins = self.Coins + coin
        return (f"Total Coins : {self.Coins}\n")

    # Die
    def die(self, count):
        if count > self.Lives:
            return "Game Over"
        else:
            if self.Lives == 0:
                return "Game Over"
            else:
                self.Lives = self.Lives - count
            if count > self.Lives:
                return "Game Over"
            else:
                return f"Remaining Lives : {self.Lives}\n"

    # Get Multiplier
    def multiplier(self, value):
        self.Multiplier = value
        return f"Multiplier : {self.Multiplier}\n"

# Demo
objMario = Mario(3, 0, 1)
print("Collecting 400 Coins")
print(objMario.coins_collect(400))

print("Dieing:")
# First Time Dieing
print("Killed By Bot 1")
print(objMario.die(1))
# Second Time
print("Killed By Falling!")
print(objMario.die(1))
# Third Time
print("Killed by Fire!")
print(objMario.die(1))
print("\n")
# Getting Multiplier
print("Getting x2 Multiplier")
print(objMario.multiplier(2))
print("Getting x4 Multiplier")
print(objMario.multiplier(4))




