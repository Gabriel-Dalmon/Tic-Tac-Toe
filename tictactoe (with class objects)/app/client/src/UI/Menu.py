import pygame
from src.UI.Button import *

class Menu:

    def __init__(self, container, *btns):
        self.container = container
        self.btnList = []
        self.mainFont = ('freesansbold.ttf', 32)
        self.largeFont = ('freesansbold.ttf',50)

        self.hovered = None

        for btnId in range ( len(btns)): #init buttons
            self.btnList.append(Button(btns[btnId][0], btns[btnId][1]))
            self.placeBtn(btnId)

    def btnDefault(self, btnId): #reset selected button to its default state/font
        self.btnList[btnId].fontUpdate(self.mainFont, "white")
        self.placeBtn(btnId)

    def btnHovered(self, btnId):
        self.btnList[btnId].fontUpdate(self.largeFont, "white")
        self.placeBtn(btnId)

    def placeBtn(self, btnId):
        self.btnList[btnId].rect.center = (self.container.get_width() // 2, self.container.get_height() // 4 * (1 + (btnId * 0.4)))

    def isHovering(self, btnId, pos):
        if(self.btnList[btnId].rect.collidepoint(pos)):
            self.hovered = btnId
            return True

    def btnBlit(self, btnId):
        self.btnList[btnId].blitSelf(self.container)

    def blitAll(self):
        for btnId in range (len(self.btnList)):
            self.btnBlit(btnId)

#This function is called to check if a button is hovered or clicked and apply the different visual effects or return an action to call.
    def eventHandler(self, type, pos): #get event type and pos
        for btnId in range (len(self.btnList)): #iterate all the buttons of the menu
            if self.isHovering(btnId, pos): #if the iterated button is hovered
                if type == pygame.MOUSEBUTTONDOWN: #if the event type = mouse click
                    return self.btnList[btnId].command
                elif type == pygame.MOUSEMOTION: #if the event type = mouse motion
                    self.btnHovered(btnId)
                    return None

        if (self.hovered != None):
            self.btnDefault(self.hovered)
            self.hovered = None
        return None
