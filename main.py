#!/usr/local/bin/python3.9
# Not compatible with windows due to escape codes being used.

import curses
from config import *
from PIL import Image
import numpy as np

class ImageManager:
    """
    Class to manage images in pixel formats
    """
    def __init__(self) -> None:
        """
        Create a new ImageManager instance.
        """
        self.usedColorRange = 9 # 9 is the custom warning message. 9 means, up to 9 is currently used.
        self.usedColors = []
        self.cursesColorDict = {}

    def loadImage(self, imagePath:str) -> list: # Relies on numpy and Pillow (PIL) #TODO: remove this annoying dependency
        """
        Returns a list of the colors of each pixel in the image.
        """
        image = Image.open(imagePath, formats=["bmp"])
        imageArray = np.array(image)
        cursesColorArray = []

        for row in imageArray:
            rowArray = []
            for rgbValue in row:
                if (str(rgbValue) not in self.usedColors):
                    self.usedColors.append(str(rgbValue))
                    self.usedColorRange += 1
                    curses.init_color(self.usedColorRange, int((rgbValue[0]/255)*1000), int((rgbValue[1]/255)*1000), int((rgbValue[2]/255)*1000))
                    curses.init_pair(self.usedColorRange, self.usedColorRange, self.usedColorRange)
                    self.cursesColorDict.update({str(list(rgbValue)):self.usedColorRange})
                rowArray.append(self.cursesColorDict[str(list(rgbValue))])
            cursesColorArray.append(rowArray)
        return cursesColorArray
    
class WindowManager:
    """
    Class for each main window.
    """
    def __init__(self, scr) -> None:
        pass

def emulatedWindowSetup(height:int,width:int) -> None:
    print(f"\033[8;{height};{width}t")
    print(f"\033[3;0;0t")
    curses.resize_term(height, width)

def colorSetup() -> None:
    curses.start_color()
    curses.init_pair(9, curses.COLOR_RED, curses.COLOR_WHITE) # Warning message color.

def checkRequirements() -> dict:
    passedDict = {}
    passedDict.update({"HasColors":curses.has_colors()}) # Two below for map (:
    passedDict.update({"ChangableColors":curses.can_change_color()})
    return passedDict

def displayMap(window) -> None:
    imagePath = "/Users/maximzmudzinski/Coding/NewAdventure/images/MAPBMP.bmp"

def displayOptions(window) -> None:
    print("test")

def displayStatus(window) -> None:
    print("test")

def refreshWindows(windows:list) -> None:
    for window in windows:
        window.noutrefresh()
    curses.doupdate()

def main(stdscr) -> None:

    selectedX = 0 # Switches between 0 and 1, switches between left windows and right map window.
    selectedY = 0 # Switches between 0 and 1, switches between top status window and bottom options window.
    inMapView = False

    # Initial Setup
    stdscr.clear()
    emulatedWindowSetup(Config.HEIGHT, Config.WIDTH)
    colorSetup()
    requirements = checkRequirements()

    stdscr.addstr(0, 0, "Welcome to NEWADVENTURE, 2nd edition, maybe functional!", curses.A_BOLD)
    stdscr.addstr(1, 0, "This should only show up for an instant. If not, the windows failed to render.", curses.color_pair(9))
    stdscr.addstr(2, 0, f"{requirements}", curses.A_BOLD)

    stdscr.refresh()

    # Map loading

    ImgManager = ImageManager()
    mapImagePath = "/Users/maximzmudzinski/Coding/NewAdventure/images/MAPBMP.bmp"
    mapArray = ImgManager.loadImage(mapImagePath)

    mapPad = curses.newpad(int(Config.HEIGHT), int(Config.WIDTH))
    for y in range(0, Config.HEIGHT):
        for x in range(0, int(Config.WIDTH/2)):
            mapPad.addch(y,x, ord('@'), curses.color_pair(mapArray[y][x]))
    mapPad.refresh(0,1, 0,int(Config.WIDTH / 2), Config.HEIGHT + 1,int(Config.WIDTH-2))

    # The other windows

    statusWindow = curses.newwin(int(Config.HEIGHT/2), int(Config.WIDTH / 2 - 1), 0, 0)
    statusWindow.border()
    optionsWindow = curses.newwin(int(Config.HEIGHT/2), int(Config.WIDTH / 2 - 1), int(Config.HEIGHT / 2), 0)
    optionsWindow.border()

    refreshWindows([statusWindow, optionsWindow])

    # Main loop
    while True:
        key = stdscr.getch() # Get a keystroke
        if 0 < key < 256:
            key = chr(key)
            if key in ' \n':
                displayMap()
            elif key in 'Qq':
                break
            else:
                # Ignore incorrect keys
                pass
        elif key == curses.KEY_UP:
            if not inMapView and selectedY == 1:  selectedY = 0
        elif key == curses.KEY_DOWN:
            if not inMapView and selectedY == 0:  selectedY = 1
        elif key == curses.KEY_LEFT:
            if not inMapView and selectedX == 1:  selectedX = 0
        elif key == curses.KEY_RIGHT:
            if not inMapView and selectedX == 0:  selectedX = 1
        elif key == curses.KEY_RESIZE:
            emulatedWindowSetup(Config.HEIGHT, Config.WIDTH)
        else:
            # Ignore incorrect keys
            pass

if __name__ == '__main__':
    curses.wrapper(main)