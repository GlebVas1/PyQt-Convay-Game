defaultBinary = [(49, 49, 49), (255, 249, 207)]
defaultTernar = [(49, 49, 49), (128, 120, 101), (255, 249, 207)]
defaultQuadro = [(49, 49, 49),(64, 60, 50),(128, 120, 101),(255, 249, 207)]


coralQuadro = [(113, 115, 100),(111, 134, 157),(242, 99, 90),(90, 166, 242)]
redPenta = [(70, 48, 46), (112, 60, 56), (115, 58, 52), (197, 44, 33), (240, 18, 1)]

def convertColorToQTString(color):
    return 'rgb({},{},{})'.format(color[0], color[1], color[2])