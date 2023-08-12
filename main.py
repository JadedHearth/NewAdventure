#!/usr/local/bin/python3.9
# Not compatible with windows due to escape codes being used.

from config import *
from mainWindows.StatusManager import StatusManager
from mainWindows.OptionsManager import OptionsManager
from mainWindows.MapManager import MapManager

import curses

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

def doPrerefresh(windows:list) -> None:
    for window in windows:
        window.prerefresh()

def main(stdscr) -> None:
    inMapView = False

    # Initial Screen
    stdscr.clear()
    emulatedWindowSetup(Config.HEIGHT, Config.WIDTH)
    colorSetup()
    requirements = checkRequirements()

    stdscr.addstr(0, 0, "Welcome to NEWADVENTURE, 2nd edition, maybe functional!", curses.A_BOLD)
    stdscr.addstr(1, 0, "This should only show up for an instant. If not, the windows failed to render.", curses.color_pair(9))
    stdscr.addstr(2, 0, f"{requirements}", curses.A_BOLD)

    stdscr.refresh()

    # Init of windows

    mapWindow = MapManager()
    statusWindow = StatusManager()
    optionsWindow = OptionsManager()
    doPrerefresh([mapWindow, statusWindow, optionsWindow])
    curses.doupdate()

    # Main loop
    while True:
        key = stdscr.getch() # Get a keystroke
        if 0 < key < 256:
            key = chr(key)
            if key in ' \n':
                pass
            elif key in 'Qq':
                break
            elif key in "Mm":
                if inMapView: 
                    inMapView = False 
                else: 
                    inMapView = True
            elif key in "Xx":
                mapWindow.switchMap()
            else:
                # Ignore incorrect keys
                pass
        elif key == curses.KEY_UP:
            if inMapView: mapWindow.moveMap(move_y=-1)
            else: optionsWindow.changeOptions(1)
        elif key == curses.KEY_DOWN:
            if inMapView: mapWindow.moveMap(move_y=1)
            else: optionsWindow.changeOptions(0)
        elif key == curses.KEY_LEFT:
            if inMapView: mapWindow.moveMap(move_x=1)
        elif key == curses.KEY_RIGHT:
            if inMapView: mapWindow.moveMap(move_x=-1)
        elif key == curses.KEY_RESIZE: # does not currently work properly. Need to rerender the rest.
            emulatedWindowSetup(Config.HEIGHT, Config.WIDTH)
            doPrerefresh([mapWindow, statusWindow, optionsWindow])
        else:
            # Ignore incorrect keys
            pass
        curses.doupdate()

if __name__ == '__main__':
    curses.wrapper(main)