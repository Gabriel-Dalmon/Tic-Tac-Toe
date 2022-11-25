import pygame

class Button:

    def __init__(self, content, command, mainFont: tuple = ('freesansbold.ttf', 32)):
        self.content = content
        self.command = command
        self.mainFont = mainFont
        self.fontUpdate(self.mainFont,"white") #inits self.text and self.rect

    def surfaceUpdate(self):
        self.rect = self.text.get_rect()

    def fontUpdate(self, font, color):
        font = pygame.font.Font(font[0], font[1])
        self.text = font.render(self.content, True, color)
        self.surfaceUpdate()

    def blitSelf(self, container):
        container.blit(self.text, self.rect)

if __name__ == "__main__":
    win = pygame.init()
    Button("SinglePlayer", "function")





#btnRect.center = (self.container.get_width() // 2, self.container.get_height() // 4 * (1 + (btnId * 0.4))) 