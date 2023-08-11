""" The options window. """

import curses
from curses import panel
from config import *

class OptionsManager:
    """
    Class for the options window.
    """
    def __init__(self) -> None:
        self.optionsWindow = curses.newwin(int(Config.HEIGHT/2 - 2), int(Config.WIDTH / 2 - 1), int(Config.HEIGHT / 2 + 2), 0)
        self.optionsWindow.border()

        # TODO: REDO needed. Fucntion for refreshing a bunch of windows reimplemented + programmatic way of creating submenus?

        self.regularMenu = self.Menu(["Button 1", "your mommanfeaoife","Button 1","Button 1","Button 1","Button 1","Button 1","Button 1","Button 1","Button 1"])

        self.moveMenu = self.Menu(["Button cat", "Button pinata","Button 1","Button 1","Button 1","Button 1","Button 1",])

        self.menuPanelList:panel = [self.regularMenu, self.moveMenu]
        self.regularMenu.top()


    class Menu: # TODO make buttons connected to.. uh .. functions?
        def __init__(self, buttonList:list) -> None:
            """
            Creates the graphics for the buttons.
            """

            self.windowHeight = int(Config.HEIGHT / 2 - 2)
            self.windowWidth = int(Config.WIDTH / 6 - 1)

            self.buttonNames = buttonList

            self.menuWindow = curses.newwin(self.windowHeight, self.windowWidth, int(Config.HEIGHT / 2 + 2), 0)
            self.menuWindow.border()
            self.menuPanel = panel.new_panel(self.menuWindow) 


        
        def top(self) -> None:
            self.menuPanel.top()

        def noutrefresh(self) -> None:
            # TODO: make this dynamic for any size, or at least a set few sizes.
            # In the setup of my screen, there is:

            # A) space for 10 of: 
            # ---------------
            #     text
            # ---------------
            #     text
            # ---------------

            # B) space for ? of:
            # ---------------
            #     text
            # ---------------
            # ---------------
            #     text
            # ---------------

            # C) space for 10 of:
            # ---------------
            #
            #     TEXT
            #
            # ---------------


            self.heightOfEach = 2 # B

            i = 0
            for button in self.buttonNames:
                self.menuWindow.addstr(self.heightOfEach * i, 1, "─" * (self.windowWidth - 2))

                textStart = int((self.windowWidth - len(button)) / 2)
                self.menuWindow.addstr((self.heightOfEach * i) + 1, textStart, button) 
                
                i += 1
            
            self.menuWindow.noutrefresh()

    def prerefresh(self) -> None:
        self.optionsWindow.noutrefresh()
        self.regularMenu.noutrefresh()
        self.moveMenu.noutrefresh()
        panel.update_panels()
        
    def changeOptions(self, chosenOption:int) -> None:
        self.menuPanelList[chosenOption].top()
        panel.update_panels()