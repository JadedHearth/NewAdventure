from pathlib import Path

class Config:
    # My height and width is catered specifically for my computer (;
    # Probably has to be even
    # nvm you aren't allowed to change this now, the map image relies on it.
    HEIGHT = 46
    WIDTH = 204

class FileLocation:
    MAPIMAGE = Path(f"{__file__}/../images/MAPBMP.bmp/MAPBMP.bmp").parent.resolve()
    BIGMAPIMAGE = Path(f"{__file__}/../images/LARGEMAP.bmp/LARGEMAP.bmp").parent.resolve()

    