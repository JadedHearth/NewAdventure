""" The map window. """

import curses
from config import *
from utils import ImageManager

class MapManager:
    """
    Class for the map window.
    """
    def __init__(self) -> None:
        self.ImgManager = ImageManager()
        self.mapArray = self.ImgManager.loadImage(FileLocation.MAPIMAGE)
        self.mapPad = curses.newpad(int(Config.HEIGHT), int(Config.WIDTH))

    def prerefresh(self) -> None:
        for y in range(0, Config.HEIGHT):
            for x in range(0, int(Config.WIDTH/2)):
                self.mapPad.addch(y,x, ord(' '), curses.color_pair(self.mapArray[y][x]))
        self.mapPad.noutrefresh(0,1, 0,int(Config.WIDTH / 2), Config.HEIGHT + 1,int(Config.WIDTH-2))