from random import choice

class Background():
    def __init__(self, name, image, pokemonSpawns, disallowedRegions):
        self._name = name
        self._image = image
        self._pokemonSpawns = pokemonSpawns
        self._left = None
        self._right = None
        self._beneath = None
        self._above = None
        self._disallowedRegions = disallowedRegions

    def getName(self):
        return self._name

    def getImage(self):
        return self._image

    def getAllPokemonSpawns(self):
        return self._pokemonSpawns

    def getRandomPokemonSpawn(self):
        return choice(self.getAllPokemonSpawns())

    def setLeft(self, left):
        self._left = left

    def getLeft(self):
        return self._left
    
    def setRight(self, right):
        self._right = right

    def getRight(self):
        return self._right

    def setBeneath(self, beneath):
        self._beneath = beneath

    def getBeneath(self):
        return self._beneath

    def setAbove(self, above):
        self._above = above

    def getAbove(self):
        return self._above

    def isDisallowedRegion(self, x, y):
        for region in self._disallowedRegions:
            if region[0] < x < region[2] and region[1] < y < region[3]:
                return True
        return False

def getMaps():
    return [forest, spawn, city, meadow, canyon]

def getFirstMap():
    return spawn

forest = Background(
    "Forest", 
    "assets/maps/forest.png", 
    [
        [195, 155]
    ],
    [
        [120, 175, 190, 225],
        [210, 175, 280, 225],
        [120, 85, 185, 135],
        [210, 85, 275, 135],
        [125, 260, 400, 400],
        [0, 0, 90, 230],
        [0, 260, 90, 400],
        [305, 0, 400, 230],
        [90, 0, 260, 50]
    ]
)
spawn = Background(
    "Spawn", 
    "assets/maps/spawn.png", 
    [
        [155, 205], 
        [155, 290], 
        [245, 290], 
        [245, 205]
    ],
    [
        [160, 40, 240, 115], 
        [190, 220, 225, 250]
    ]
)
city = Background(
    "City", 
    "assets/maps/city.png", 
    [
        [160, 110]
    ], 
    [
        [25, 40, 85, 120],
        [85, 5, 150, 120],
        [0, 185, 185, 235],
        [0, 260, 185, 400],
        [225, 195, 280, 400],
        [225, 0, 400, 165],
        [310, 315, 365, 365]
    ]
)
meadow = Background(
    "Meadow", 
    "assets/maps/meadow.png", 
    [
        [95, 255]
    ], 
    [
        [0, 325, 40, 380],
        [40, 335, 100, 390],
        [100, 325, 120, 380],
        [120, 315, 175, 370],
        [160, 310, 215, 360],
        [190, 295, 235, 335],
        [195, 280, 250, 310],
        [195, 200, 250, 230],
        [185, 160, 240, 200],
        [180, 125, 235, 160],
        [190, 85, 245, 125],
        [200, 50, 250, 85],
        [205, 15, 260, 50],
        [215, 0, 270, 15]
    ]
)
canyon = Background(
    "Canyon",
    "assets/maps/canyon.png",
    [
        [190, 220]
    ],
    [
        [250, 0, 355, 35],
        [245, 35, 350, 70],
        [240, 70, 345, 110],
        [245, 105, 350, 140],
        [240, 145, 345, 175],
        [235, 180, 340, 215],
        [230, 220, 335, 220],
        [230, 275, 340, 300],
        [235, 300, 345, 335],
        [240, 335, 350, 370],
        [245, 370, 355, 390],
        [250, 400, 360, 400]
    ]
)

forest.setRight(spawn)
forest.setBeneath(meadow)

spawn.setLeft(forest)
spawn.setBeneath(canyon)
spawn.setRight(city)

city.setLeft(spawn)

meadow.setAbove(forest)
meadow.setRight(canyon)

canyon.setLeft(meadow)
canyon.setAbove(spawn)