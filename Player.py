class Player:

    def __init__(self, name):
        self.name = name

    def chooseSpot(self):
        x = int(input("X: "))
        y = int(input("Y: "))
        return (x,y)