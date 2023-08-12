""" Utility library """

from config import *

import curses
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

    def loadImage(self, imagePath) -> list: # Relies on numpy and Pillow (PIL) 
        """
        Returns a list of the colors of each pixel in the image.
        TODO LT: remove these annoying dependencies. Numpy *should* be the easier one to remove, but both should be possible.
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
    
