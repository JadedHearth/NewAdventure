""" The map window. """

import curses
from config import *
from utils import ImageManager

class MapManager:
    """
    Class for the map window.
    """
    def __init__(self) -> None:
        self.whichMap = FileLocation.MAPIMAGE
        self.ImgManager = ImageManager()
        self.mapArray = self.ImgManager.loadImage(self.whichMap)
        self.mapPad = curses.newpad(int(Config.HEIGHT), int(Config.WIDTH))
        self.y_location = 0
        self.x_location = 1

    def prerefresh(self) -> None:
        for y in range(0, Config.HEIGHT):
            for x in range(0, int(Config.WIDTH/2)):
                self.mapPad.addch(y,x, ord(' '), curses.color_pair(self.mapArray[y][x]))
        self.mapPad.noutrefresh(self.y_location,self.x_location, 0,int(Config.WIDTH / 2), Config.HEIGHT + 1,int(Config.WIDTH-2))

    def moveMap(self, move_y=0, move_x=0) -> None:
        self.y_location += move_y
        self.x_location += move_x
        self.prerefresh()

    def switchMap(self) -> None:
        if self.whichMap == FileLocation.MAPIMAGE: self.whichMap = FileLocation.BIGMAPIMAGE
        else: self.whichMap = FileLocation.MAPIMAGE
        self.mapArray = self.ImgManager.loadImage(self.whichMap)
        self.prerefresh()
