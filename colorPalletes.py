defaultBinary = [(49, 49, 49), (255, 249, 207)]
defaultTernar = [(49, 49, 49), (128, 120, 101), (255, 249, 207)]


defaultQuadro = [(49, 49, 49),(64, 60, 50),(128, 120, 101),(255, 249, 207)]
lazureQuadro = [(49, 49, 49),(62, 110, 133),(29, 155, 218),(0, 164, 249)]


coralQuadro = [(113, 115, 100),(111, 134, 157),(242, 99, 90),(90, 166, 242)]
redPenta = [(70, 48, 46), (112, 60, 56), (115, 58, 52), (197, 44, 33), (240, 18, 1)]
limeQuadro = [(49, 49, 49), (110, 133, 62), (155, 218, 29), (237, 255, 200)]
greenHexa = [(33, 56, 46), (46, 70, 60), (56, 112, 88), (52, 155, 110), (33, 197, 126), (0, 240, 136)]

colorPalletesDict = {"Yellow chalk 2" : defaultBinary,
                    "Yellow chalk 3" : defaultTernar, 
                    "Yellow chunk 4" : defaultQuadro, 
                    "Lazure 4" : lazureQuadro,
                    "Lime 4" : limeQuadro, 
                    "Coral 4" : coralQuadro,
                    "Red 5" : redPenta, 
                    "Green 6" : greenHexa}

def convertColorToQTString(color) -> str:
    return 'rgb({},{},{})'.format(color[0], color[1], color[2])

def convertPalleteToQT(pallete : list) -> list:
    return ['rgb({},{},{})'.format(color[0], color[1], color[2]) for color in pallete]