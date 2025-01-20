defaultBinary = [(49, 49, 49), (255, 249, 207)]
defaultTernar = [(49, 49, 49), (128, 120, 101), (255, 249, 207)]


defaultQuadro = [(49, 49, 49),(64, 60, 50),(128, 120, 101),(255, 249, 207)]
lazureQuadro = [(49, 49, 49),(62, 110, 133),(29, 155, 218),(0, 164, 249)]


coralQuadro = [(113, 115, 100),(111, 134, 157),(242, 99, 90),(90, 166, 242)]
redPenta = [(70, 48, 46), (112, 60, 56), (115, 58, 52), (197, 44, 33), (240, 18, 1)]
limeQuadro = [(49, 49, 49), (110, 133, 62), (155, 218, 29), (237, 255, 200)]
greenHexa = [(33, 56, 46), (46, 70, 60), (56, 112, 88), (52, 155, 110), (33, 197, 126), (0, 240, 136)]

elf8 = [(49, 49, 49),
        (40, 87, 87), 
        (23, 204, 204), 
        (154, 194, 224), 
        (167, 207, 237), 
        (233, 182, 210), 
        (245, 182, 210), 
        (255, 194, 214)]

fuxia5 = [(49, 49, 49), 
          (69, 54, 66), 
          (113, 43, 69), 
          (169, 12, 85), 
          (250, 0, 117)]

seaWater6 = [(49, 49, 49), 
             (34, 40, 65), 
             (34, 62, 102), 
             (34, 104, 139), 
             (28, 184, 189), 
             (38, 226, 163)]
autumn7 =  [(49, 49, 49),
           (98, 69, 53),
           (196, 109, 61),
           (245, 129, 65),
           (247, 142, 63),
           (253, 168, 57),
           (255, 181, 55)]
# rgb(38, 226, 163)
summer7 = [(49, 49, 49),
          (68, 94, 69),
          (68, 94, 87),
          (94, 69, 68),
          (222, 57, 49),
          (49, 222, 55),
          (0, 224, 159)]

blueOrange = [(60, 80, 85),
              (128, 100, 73),
              (69, 146, 170),
              (255, 136, 18),
              (191, 126, 61),
              (0, 197, 255)]

colorPalletesDict = {"Yellow chalk 2" : defaultBinary,
                    "Yellow chalk 3" : defaultTernar, 
                    "Yellow chunk 4" : defaultQuadro, 
                    "Lazure 4" : lazureQuadro,
                    "Lime 4" : limeQuadro, 
                    "Coral 4" : coralQuadro,
                    "Red 5" : redPenta, 
                    "Green 6" : greenHexa,
                    "Elf 8" : elf8,
                    "Fuxia 5" : fuxia5,
                    "Sea water 6" : seaWater6,
                    "Autumn 7" : autumn7,
                    "Summer 7" : summer7,
                    "Blue/Orange 6" : blueOrange}

def convertColorToQTString(color) -> str:
    return 'rgb({},{},{})'.format(color[0], color[1], color[2])

def convertPalleteToQT(pallete : list) -> list:
    return ['rgb({},{},{})'.format(color[0], color[1], color[2]) for color in pallete]