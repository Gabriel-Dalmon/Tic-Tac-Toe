class Player:

    def __init__(self, name):
        self.name = name
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

    def chooseSpot(self):
        x = int(input("X: "))
        y = int(input("Y: "))
        return (x,y)